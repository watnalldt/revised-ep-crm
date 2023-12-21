from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from rangefilter.filters import DateRangeFilter

from clients.models import Client
from utilities.models import Supplier, Utility

from .models import Contract

User = get_user_model()


class ContractResource(resources.ModelResource):
    client = fields.Field(
        column_name="client",
        attribute="client",
        widget=ForeignKeyWidget(Client, "client"),
    )

    property_manager = fields.Field(
        column_name="property_manager",
        attribute="property_manager",
        widget=ForeignKeyWidget(User, "email"),
    )

    supplier = fields.Field(
        column_name="supplier",
        attribute="supplier",
        widget=ForeignKeyWidget(Supplier, "supplier"),
    )

    utility = fields.Field(
        column_name="utility",
        attribute="utility",
        widget=ForeignKeyWidget(Utility, "utility"),
    )
    future_supplier = fields.Field(
        column_name="future_supplier",
        attribute="future_supplier",
        widget=ForeignKeyWidget(Supplier, "supplier"),
    )

    class Meta:
        model = Contract
        report_skipped = True
        import_id_fields = ("id",)
        export_order = [
            "id",
            "contract_type",
            "contract_status",
            "dwellent_id",
            "bid_id",
            "portal_status",
            "client",
            "property_manager",
            "is_directors_approval",
            "business_name",
            "company_reg_number",
            "utility",
            "top_line",
            "mpan_mpr",
            "second_mpan_mpr",
            "meter_status",
            "meter_serial_number",
            "building_name",
            "site_address",
            "billing_address",
            "supplier",
            "reference_4",
            "contract_start_date",
            "contract_end_date",
            "supplier_start_date",
            "account_number",
            "eac",
            "day_consumption",
            "night_consumption",
            "vat",
            "vat_declaration_sent",
            "vat_declaration_date",
            "vat_declaration_expires",
            "contract_value",
            "standing_charge",
            "sc_frequency",
            "unit_rate_1",
            "unit_rate_2",
            "unit_rate_3",
            "feed_in_tariff",
            "seamless_status",
            "profile",
            "is_ooc",
            "service_type",
            "pence_per_kilowatt",
            "day_kilowatt_hour_rate",
            "night_rate",
            "annualised_budget",
            "commission_per_annum",
            "commission_per_unit",
            "commission_per_contract",
            "partner_commission",
            "smart_meter",
            "notes",
            "kva",
            "future_supplier",
            "future_contract_start_date",
            "future_contract_end_date",
            "future_unit_rate_1",
            "future_unit_rate_2",
            "future_unit_rate_3",
            "future_standing_charge",
        ]


class ClientFilter(AutocompleteFilter):
    title = "Client"  # display title
    field_name = "client"  # name of the foreign key field


class PropertyManagerFilter(AutocompleteFilter):
    title = "Property Manager"  # display title
    field_name = "property_manager"  # name of the foreign key field


class SupplierFilter(AutocompleteFilter):
    title = "Supplier"  # display title
    field_name = "supplier"  # name of the foreign key field


class UtilityTypeFilter(AutocompleteFilter):
    title = "Utility Type"  # display title
    field_name = "utility"  # name of the foreign key field


# class AccountManagerFilter(admin.SimpleListFilter):
#     title = 'Account Manager'
#     parameter_name = 'account_manager'
#
#     def lookups(self, request, model_admin):
#         # Get a distinct list of account managers for available contracts
#         account_managers = (
#             model_admin.get_queryset(request)
#             .values_list('client__account_manager__email', flat=True)
#             .distinct()
#         )
#
#         # Return only one tuple for the selected account manager (if any)
#         selected_value = self.value()
#         if selected_value:
#             return ((selected_value, selected_value),)
#
#         return tuple((am, am) for am in account_managers)
#
#     def queryset(self, request, queryset):
#         # Filter contracts based on selected account manager or show all contracts for all account managers
#         value = self.value()
#         if value:
#             # Filter the queryset for the selected account manager
#             queryset = queryset.filter(client__account_manager__email=value)
#         return queryset


class ContractAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    show_full_result_count = False
    resource_class = ContractResource
    list_per_page = 10
    ordering = ("client",)
    list_display = (
        "id",
        "contract_status",
        # "link_to_clients",
        "business_name",
        "property_manager",
        "site_address",
        "supplier",
        "utility",
        "mpan_mpr",
        "second_mpan_mpr",
        "meter_serial_number",
        "eac",
        "contract_start_date",
        "contract_end_date",
        "is_ooc",
    )
    list_display_links = ("business_name",)
    list_select_related = ("client", "property_manager", "supplier", "utility")
    fieldsets = (
        (
            "Site Information",
            {
                "description": "Enter the site details",
                "fields": (
                    ("client", "property_manager", "business_name"),
                    "site_address",
                    "supplier",
                    "utility",
                    "meter_serial_number",
                    "mpan_mpr",
                    "top_line",
                    "vat",
                    "vat_declaration_sent",
                    "vat_declaration_date",
                    "vat_declaration_expires",
                ),
            },
        ),
        (
            "Contract Information",
            {
                "description": "Contract Information",
                "fields": (
                    (
                        "account_number",
                        "company_reg_number",
                    ),
                    "is_directors_approval",
                    "contract_type",
                    "contract_status",
                ),
            },
        ),
        (
            "Contract Date Details",
            {
                "description": "Enter the following details",
                "fields": (
                    (
                        "contract_start_date",
                        "contract_end_date",
                        "supplier_start_date",
                    ),
                    "is_ooc",
                ),
            },
        ),
        (
            "Seamless Contract Information",
            {
                "description": "The following only applies to seamless contracts",
                "classes": ("collapse",),
                "fields": (
                    (
                        "dwellent_id",
                        "bid_id",
                        "portal_status",
                        "reference_4",
                    ),
                    ("building_name", "billing_address"),
                    ("day_consumption", "night_consumption", "contract_value"),
                    ("standing_charge", "sc_frequency"),
                    ("unit_rate_1", "unit_rate_2", "unit_rate_3"),
                    "seamless_status",
                ),
            },
        ),
        (
            "Service Information",
            {
                "description": "Enter the following data",
                "fields": ("eac", "kva", "profile", "service_type", "feed_in_tariff"),
            },
        ),
        (
            "Rates",
            {
                "description": "Enter the following data",
                "fields": (
                    "pence_per_kilowatt",
                    "day_kilowatt_hour_rate",
                    "night_rate",
                    "annualised_budget",
                ),
            },
        ),
        (
            "Commissions",
            {
                "description": "Enter the following",
                "fields": (
                    "commission_per_annum",
                    "commission_per_unit",
                    "partner_commission",
                ),
            },
        ),
        (
            "Future Contract Information",
            {
                "description": "Enter future contract information",
                "fields": (
                    "future_contract_start_date",
                    "future_contract_end_date",
                    "future_supplier",
                    "future_unit_rate_1",
                    "future_unit_rate_2",
                    "future_unit_rate_3",
                    "future_standing_charge",
                ),
            },
        ),
        ("Notes", {"description": "Additional Information", "fields": ("notes",)}),
    )
    list_filter = [
        "contract_type",
        "contract_status",
        "client",
        PropertyManagerFilter,
        SupplierFilter,
        UtilityTypeFilter,
        # AccountManagerFilter,
        "seamless_status",
        "is_ooc",
        "is_directors_approval",
        "meter_status",
        ("contract_end_date", DateRangeFilter),
        ("contract_start_date", DateRangeFilter),
        "vat",
        "vat_declaration_sent",
    ]
    autocomplete_fields = [
        "client",
        # "client_manager",
        "supplier",
        "future_supplier",
    ]
    search_help_text = "Search by MPAN/MPR or Business Name, Client Name, Meter Serial Number"
    search_fields = (
        "business_name",
        "client__client",
        "utility__utility",
        "supplier__supplier",
        "mpan_mpr",
        "second_mpan_mpr",
        "meter_serial_number",
        "site_address",
    )
    date_hierarchy = "contract_end_date"

    actions = [
        "directors_approval_required",
        "directors_approval_granted",
        "contracts_lost",
        "change_contract_to_seamless",
        "change_contract_to_non_seamless",
        "make_contract_live",
        "make_contract_pricing",
        "make_contract_objection",
        "make_contract_locked",
        "make_vat_declaration",
    ]

    @admin.action(description="Make Live")
    def make_contract_live(self, request, queryset):
        queryset.update(contract_status="LIVE")

    @admin.action(description="Pricing")
    def make_contract_pricing(self, request, queryset):
        queryset.update(contract_status="PRICING")

    @admin.action(description="Objection")
    def make_contract_objection(self, request, queryset):
        queryset.update(contract_status="OBJECTION")

    @admin.action(description="Locked")
    def make_contract_locked(self, request, queryset):
        queryset.update(contract_status="LOCKED")

    @admin.action(description="Directors Approval Granted")
    def directors_approval_granted(self, request, queryset):
        queryset.update(is_directors_approval=False)

    @admin.action(description="Directors Approval Required")
    def directors_approval_required(self, request, queryset):
        queryset.update(is_directors_approval=True)

    @admin.action(description="Contract Removed")
    def contracts_lost(self, request, queryset):
        queryset.update(contract_status="REMOVED")

    @admin.action(description="Make Seamless")
    def change_contract_to_seamless(self, request, queryset):
        queryset.update(contract_type="SEAMLESS")

    @admin.action(description="Make Non-Seamless")
    def change_contract_to_non_seamless(self, request, queryset):
        queryset.update(contract_type="NON_SEAMLESS")

    # @admin.action(description="Deactivate Meter")
    # def deactivate_meter(self, request, queryset):
    #     queryset.update(meter_deactivated=True)

    @admin.action(description="Vat Declaration Sent")
    def make_vat_declaration(self, request, queryset):
        for obj in queryset:
            # Check if the vat_declaration_date field is not filled or is None
            if obj.vat_declaration_date is None or not obj.vat_declaration_date.strip():
                self.message_user(
                    request,
                    f"Vat declaration date is not filled for {obj}. Update aborted.",
                    level="ERROR",
                )
            else:
                obj.vat_declaration_sent = "YES"
                obj.save()
                self.message_user(request, f"Vat declaration set to YES for {obj}.")

    # def link_to_clients(self, obj):
    #     link = reverse("admin:clients_client_change", args=[obj.client.id])
    #     return format_html(
    #         '<a href="{}">{}</a>',
    #         link,
    #         obj.client,
    #     )
    #
    # link_to_clients.short_description = "Clients"


admin.site.register(Contract, ContractAdmin)
