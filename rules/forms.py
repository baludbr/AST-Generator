# rules/forms.py
from django import forms
from .models import Rule

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['rule_string']

class CombineRulesForm(forms.Form):
    rule_ids = forms.CharField(label='Rule IDs (comma-separated)', max_length=255)

class EvaluateRuleForm(forms.Form):
    mega_rule_id = forms.IntegerField(label='Mega Rule ID')
    data = forms.CharField(widget=forms.Textarea, label='Data (JSON)')

class ModifyRuleForm(forms.Form):
    rule_id = forms.IntegerField(label='Rule ID')
    new_rule_string = forms.CharField(label='New Rule String', max_length=255)
