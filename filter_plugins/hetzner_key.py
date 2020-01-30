from ansible_filter import form_urlencode
from ansible_filter import change_set


class FilterModule(object):

    def filters(self):
        return {
            'hetzner_key_form_urlencode': form_urlencode.form_urlencode,
            'hetzner_key_change_set': change_set.change_set
        }
