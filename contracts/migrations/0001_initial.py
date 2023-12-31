# Generated by Django 4.2.8 on 2023-12-20 15:48

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models

import contracts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('utilities', '0001_initial'),
        ('users', '0003_propertymanager'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalContract',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('contract_type', models.CharField(choices=[('SEAMLESS', 'Seamless'), ('NON_SEAMLESS', 'Non-Seamless')], default='SEAMLESS', max_length=20)),
                ('contract_status', models.CharField(choices=[('LIVE', 'Live'), ('REMOVED', 'Removed'), ('LOCKED', 'Locked'), ('PRICING', 'Pricing'), ('OBJECTION', 'Objection'), ('NEW', 'New')], default='LIVE', max_length=20)),
                ('dwellent_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dwellent ID')),
                ('bid_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='BID ID')),
                ('portal_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Portal Status')),
                ('is_directors_approval', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=4, verbose_name='Directors Approval')),
                ('business_name', models.CharField(max_length=255, verbose_name='Business Name')),
                ('company_reg_number', models.CharField(blank=True, max_length=250, null=True, verbose_name='Company Reg Number')),
                ('top_line', models.CharField(blank=True, max_length=40, null=True, verbose_name='Top Line')),
                ('mpan_mpr', models.IntegerField(validators=[contracts.models.validate_no_decimal], verbose_name='MPAN/MPR')),
                ('meter_serial_number', models.CharField(blank=True, help_text="<a href='https://www.ecoes.co.uk' target='_blank'>Look up Meter Serial Number</a>", max_length=100, null=True)),
                ('meter_status', models.CharField(choices=[('ACTIVE', 'Active'), ('DE_ENERGISED', 'De-Energised'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=15, verbose_name='Meter Status')),
                ('building_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Building Name')),
                ('site_address', models.TextField(blank=True, null=True, verbose_name='Site Address')),
                ('billing_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing Address')),
                ('reference_4', models.CharField(blank=True, max_length=50, null=True)),
                ('contract_start_date', models.DateField(blank=True, null=True, verbose_name='Contract Start Date')),
                ('contract_end_date', models.DateField(blank=True, null=True, verbose_name='Contract End Date')),
                ('supplier_start_date', models.DateField(blank=True, null=True, verbose_name='Supplier Start Date')),
                ('account_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Account Number')),
                ('eac', models.FloatField(blank=True, null=True, verbose_name='EAC')),
                ('day_consumption', models.FloatField(blank=True, null=True, verbose_name='Day Consumption')),
                ('night_consumption', models.FloatField(blank=True, null=True, verbose_name='Night Consumption')),
                ('kva', models.CharField(blank=True, max_length=15, null=True, verbose_name='KVA')),
                ('vat', models.CharField(blank=True, max_length=100, null=True, verbose_name='VAT')),
                ('contract_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Contract Value')),
                ('standing_charge', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Standing Charge')),
                ('sc_frequency', models.CharField(blank=True, max_length=250, null=True, verbose_name='Standing Charge Frequency')),
                ('unit_rate_1', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 1')),
                ('unit_rate_2', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 2')),
                ('unit_rate_3', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 3')),
                ('feed_in_tariff', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Feed In Tariff')),
                ('seamless_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seamless Status')),
                ('profile', models.CharField(blank=True, max_length=100, null=True, verbose_name='Profile')),
                ('is_ooc', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=4, verbose_name='Out Of Contract')),
                ('service_type', models.CharField(blank=True, max_length=50, null=True)),
                ('pence_per_kilowatt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Pence Per Kilowatt')),
                ('day_kilowatt_hour_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Day Kilowatt Hour Rate')),
                ('night_rate', models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True, verbose_name='Night Rate')),
                ('annualised_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Annualised Budget')),
                ('commission_per_annum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Annum')),
                ('commission_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Unit')),
                ('commission_per_contract', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Contract')),
                ('partner_commission', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Partner Commission')),
                ('smart_meter', models.CharField(blank=True, max_length=50, null=True, verbose_name='Smart Meter')),
                ('vat_declaration_sent', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=4, verbose_name='Vat Declaration Sent')),
                ('vat_declaration_date', models.DateField(blank=True, null=True, verbose_name='Date Sent')),
                ('vat_declaration_expires', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('future_contract_start_date', models.DateField(blank=True, null=True, verbose_name='Future Contract Start Date')),
                ('future_contract_end_date', models.DateField(blank=True, null=True, verbose_name='Future Contract End Date')),
                ('future_unit_rate_1', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 1')),
                ('future_unit_rate_2', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 2')),
                ('future_unit_rate_3', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 3')),
                ('future_standing_charge', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Standing Charge')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='clients.client', verbose_name='Client Name')),
                ('future_supplier', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utilities.supplier', verbose_name='Future Supplier')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('property_manager', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='users.propertymanager', verbose_name='Property Manager')),
                ('supplier', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utilities.supplier', verbose_name='Supplier Name')),
                ('utility', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utilities.utility', verbose_name='Utility Type')),
            ],
            options={
                'verbose_name': 'historical Client Contract',
                'verbose_name_plural': 'historical Client Contracts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.CharField(choices=[('SEAMLESS', 'Seamless'), ('NON_SEAMLESS', 'Non-Seamless')], default='SEAMLESS', max_length=20)),
                ('contract_status', models.CharField(choices=[('LIVE', 'Live'), ('REMOVED', 'Removed'), ('LOCKED', 'Locked'), ('PRICING', 'Pricing'), ('OBJECTION', 'Objection'), ('NEW', 'New')], default='LIVE', max_length=20)),
                ('dwellent_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dwellent ID')),
                ('bid_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='BID ID')),
                ('portal_status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Portal Status')),
                ('is_directors_approval', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=4, verbose_name='Directors Approval')),
                ('business_name', models.CharField(max_length=255, verbose_name='Business Name')),
                ('company_reg_number', models.CharField(blank=True, max_length=250, null=True, verbose_name='Company Reg Number')),
                ('top_line', models.CharField(blank=True, max_length=40, null=True, verbose_name='Top Line')),
                ('mpan_mpr', models.IntegerField(validators=[contracts.models.validate_no_decimal], verbose_name='MPAN/MPR')),
                ('meter_serial_number', models.CharField(blank=True, help_text="<a href='https://www.ecoes.co.uk' target='_blank'>Look up Meter Serial Number</a>", max_length=100, null=True)),
                ('meter_status', models.CharField(choices=[('ACTIVE', 'Active'), ('DE_ENERGISED', 'De-Energised'), ('REMOVED', 'Removed')], default='ACTIVE', max_length=15, verbose_name='Meter Status')),
                ('building_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Building Name')),
                ('site_address', models.TextField(blank=True, null=True, verbose_name='Site Address')),
                ('billing_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Billing Address')),
                ('reference_4', models.CharField(blank=True, max_length=50, null=True)),
                ('contract_start_date', models.DateField(blank=True, null=True, verbose_name='Contract Start Date')),
                ('contract_end_date', models.DateField(blank=True, null=True, verbose_name='Contract End Date')),
                ('supplier_start_date', models.DateField(blank=True, null=True, verbose_name='Supplier Start Date')),
                ('account_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Account Number')),
                ('eac', models.FloatField(blank=True, null=True, verbose_name='EAC')),
                ('day_consumption', models.FloatField(blank=True, null=True, verbose_name='Day Consumption')),
                ('night_consumption', models.FloatField(blank=True, null=True, verbose_name='Night Consumption')),
                ('kva', models.CharField(blank=True, max_length=15, null=True, verbose_name='KVA')),
                ('vat', models.CharField(blank=True, max_length=100, null=True, verbose_name='VAT')),
                ('contract_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Contract Value')),
                ('standing_charge', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Standing Charge')),
                ('sc_frequency', models.CharField(blank=True, max_length=250, null=True, verbose_name='Standing Charge Frequency')),
                ('unit_rate_1', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 1')),
                ('unit_rate_2', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 2')),
                ('unit_rate_3', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Unit Rate 3')),
                ('feed_in_tariff', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Feed In Tariff')),
                ('seamless_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seamless Status')),
                ('profile', models.CharField(blank=True, max_length=100, null=True, verbose_name='Profile')),
                ('is_ooc', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=4, verbose_name='Out Of Contract')),
                ('service_type', models.CharField(blank=True, max_length=50, null=True)),
                ('pence_per_kilowatt', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Pence Per Kilowatt')),
                ('day_kilowatt_hour_rate', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Day Kilowatt Hour Rate')),
                ('night_rate', models.DecimalField(blank=True, decimal_places=8, max_digits=8, null=True, verbose_name='Night Rate')),
                ('annualised_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Annualised Budget')),
                ('commission_per_annum', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Annum')),
                ('commission_per_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Unit')),
                ('commission_per_contract', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Commission Per Contract')),
                ('partner_commission', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Partner Commission')),
                ('smart_meter', models.CharField(blank=True, max_length=50, null=True, verbose_name='Smart Meter')),
                ('vat_declaration_sent', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=4, verbose_name='Vat Declaration Sent')),
                ('vat_declaration_date', models.DateField(blank=True, null=True, verbose_name='Date Sent')),
                ('vat_declaration_expires', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('future_contract_start_date', models.DateField(blank=True, null=True, verbose_name='Future Contract Start Date')),
                ('future_contract_end_date', models.DateField(blank=True, null=True, verbose_name='Future Contract End Date')),
                ('future_unit_rate_1', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 1')),
                ('future_unit_rate_2', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 2')),
                ('future_unit_rate_3', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Unit Rate 3')),
                ('future_standing_charge', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True, verbose_name='Future Standing Charge')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_contracts', to='clients.client', verbose_name='Client Name')),
                ('future_supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='future_suppliers', to='utilities.supplier', verbose_name='Future Supplier')),
                ('property_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_manager_contracts', to='users.propertymanager', verbose_name='Property Manager')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_suppliers', to='utilities.supplier', verbose_name='Supplier Name')),
                ('utility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contract_utilities', to='utilities.utility', verbose_name='Utility Type')),
            ],
            options={
                'verbose_name': 'Client Contract',
                'verbose_name_plural': 'Client Contracts',
                'db_table': 'client_contracts',
                'ordering': ['contract_end_date'],
                'indexes': [models.Index(fields=['mpan_mpr'], name='client_cont_mpan_mp_61a064_idx'), models.Index(fields=['client'], name='client_cont_client__b89d8d_idx'), models.Index(fields=['-client'], name='client_cont_client__ad3c39_idx'), models.Index(fields=['business_name'], name='client_cont_busines_06b65a_idx'), models.Index(fields=['-business_name'], name='client_cont_busines_3058d6_idx')],
            },
        ),
        migrations.AddConstraint(
            model_name='contract',
            constraint=models.UniqueConstraint(fields=('mpan_mpr', 'id'), name='unique_contract'),
        ),
    ]
