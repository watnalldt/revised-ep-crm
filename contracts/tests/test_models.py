from datetime import date

import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone

from clients.models import Client
from contracts.models import (
    Contract,
    validate_no_decimal,
)
from users.models import AccountManager, PropertyManager
from utilities.models import Supplier, Utility


@pytest.fixture
def sample_account_manager():
    return AccountManager.objects.create(email="test1@example.com", password="test12345")


@pytest.fixture
def sample_property_manager():
    return PropertyManager.objects.create(email="test@example.com", password="test1234")


@pytest.fixture
def sample_client(sample_account_manager):
    return Client.objects.create(client="Test Client", account_manager=sample_account_manager)


@pytest.fixture
def sample_utility():
    return Utility.objects.create(utility="Electricity")


@pytest.fixture
def sample_supplier():
    return Supplier.objects.create(supplier="Test Supplier")


@pytest.fixture
def sample_contract(sample_client, sample_utility, sample_supplier, sample_property_manager):
    return Contract.objects.create(
        contract_type=Contract.ContractType.SEAMLESS,
        contract_status=Contract.ContractStatus.LIVE,
        client=sample_client,
        property_manager=sample_property_manager,
        is_directors_approval=Contract.DirectorsApproval.NO,
        business_name="Test Business",
        utility=sample_utility,
        mpan_mpr="0987654321",
        meter_status="Contract.MeterStatus.ACTIVE",
        meter_serial_number="A456789",
        supplier=sample_supplier,
        contract_start_date=date.today(),
        contract_end_date=date.today() + timezone.timedelta(days=30),
        account_number="Test Account Number",
        eac=100.0,
        day_consumption=50.0,
        night_consumption=30.0,
        kva="Test KVA",
        vat="Test VAT",
        contract_value=5000.0,
        standing_charge=100.0,
        sc_frequency="Monthly",
        unit_rate_1=0.15,
        unit_rate_2=0.12,
        unit_rate_3=0.10,
        feed_in_tariff=0.05,
        seamless_status="Active",
        profile="Test Profile",
        is_ooc=Contract.OutOfContract.NO,
        service_type="Test Service Type",
        pence_per_kilowatt=0.18,
        day_kilowatt_hour_rate=0.20,
        night_rate=0.08,
        annualised_budget=6000.0,
        commission_per_annum=500.0,
        commission_per_unit=0.02,
        commission_per_contract=100.0,
        partner_commission=200.0,
        smart_meter="Yes",
        vat_declaration_sent="Yes",
        vat_declaration_date=date.today(),
        vat_declaration_expires=date.today() + timezone.timedelta(days=365),
        notes="Test Notes",
        future_contract_start_date=date.today() + timezone.timedelta(days=60),
        future_contract_end_date=date.today() + timezone.timedelta(days=90),
        future_unit_rate_1=0.14,
        future_unit_rate_2=0.11,
        future_unit_rate_3=0.09,
        future_supplier=sample_supplier,
        future_standing_charge=90.0,
    )


@pytest.mark.django_db
def test_contract_str(sample_contract):
    assert str(sample_contract) == "Test Business with mpan 0987654321"


@pytest.mark.django_db
def test_days_till_property(sample_contract):
    sample_contract.contract_end_date = date.today() + timezone.timedelta(days=5)
    assert sample_contract.days_till == "5 days"


@pytest.mark.django_db
def test_validate_no_decimal_with_decimal():
    # Test with a decimal value
    with pytest.raises(ValidationError):
        validate_no_decimal(12.34)


@pytest.mark.django_db
def test_validate_no_decimal_with_integer():
    # Test with an integer value
    try:
        validate_no_decimal(1234)
    except ValidationError:
        pytest.fail("Unexpected ValidationError raised")


@pytest.mark.django_db
def test_gas_query_set():
    assert Contract.utilities.gas().count() == 0  # Assuming no gas utilities are created in fixtures

@pytest.mark.django_db
def test_contract_type_query_set():
    assert Contract.contracts.seamless().count() == 0
    assert Contract.contracts.non_seamless().count() == 0


@pytest.mark.django_db
def test_electricity_query_set():
    assert Contract.utilities.electricity().count()  == 0


@pytest.mark.django_db
def test_save_method_normal(sample_contract):
    # Test with vat_declaration_sent as YES and a valid vat_declaration_date
    sample_contract.vat_declaration_sent = Contract.VatDeclaration.YES
    sample_contract.vat_declaration_date = date.today()
    sample_contract.save()
    assert sample_contract.vat_declaration_expires == sample_contract.contract_end_date

    # Test with vat_declaration_sent as NO
    sample_contract.vat_declaration_sent = Contract.VatDeclaration.NO
    sample_contract.save()
    assert sample_contract.vat_declaration_expires is None


@pytest.mark.django_db
def test_save_method_validation_error(sample_contract):
    # Set up for raising ValueError
    sample_contract.vat_declaration_sent = Contract.VatDeclaration.YES
    sample_contract.vat_declaration_date = None

    # Check if ValueError is raised
    with pytest.raises(ValueError) as excinfo:
        sample_contract.save()
    assert "vat_declaration_date cannot be null when vat_declaration_sent is YES" in str(excinfo.value)
