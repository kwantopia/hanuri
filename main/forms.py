# -*- coding: utf-8 -*-

from django import forms
from main.models import BrokenRelationKorean, BrokenRelationEnglish


class BrokenRelationKoreanForm(forms.ModelForm):

  class Meta:
    model = BrokenRelationKorean
    exclude = ['remote_id', 'remote_addr', 'remote_host',
                'user_agent', 'referrer', 'timestamp']

  def __init__(self, *args, **kwargs):
    super(BrokenRelationKoreanForm, self).__init__(*args, **kwargs)
    self.fields['broken'].widget.attrs['placeholder'] = u"부서진 관계를 기술해 보세요"
    self.fields['broken'].widget.attrs['class'] = "input-xlarge span6"
    self.fields['restore'].widget.attrs['placeholder'] = u"올바른 관계와 믿음을 세우고 복원하는 방법을 기술해 보세요"
    self.fields['restore'].widget.attrs['class'] = "input-xlarge span6"


class BrokenRelationEnglishForm(forms.ModelForm):

  class Meta:
    model = BrokenRelationEnglish
    exclude = ['remote_id', 'remote_addr', 'remote_host',
                'user_agent', 'referrer', 'timestamp']

  def __init__(self, *args, **kwargs):
    super(BrokenRelationEnglishForm, self).__init__(*args, **kwargs)
    self.fields['broken'].widget.attrs['placeholder'] = "Please describe your broken relationship"
    self.fields['broken'].widget.attrs['class'] = "input-xlarge span6"
    self.fields['restore'].widget.attrs['placeholder'] = "Please describe how you restored your relationship"
    self.fields['restore'].widget.attrs['class'] = "input-xlarge span6"
