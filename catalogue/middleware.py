from .forms import MailingListForm

# add mailing list form to all templates
class MailingListFormMiddleware(object):

    def process_template_response(self, request, response):
        response.context_data['form'] = MailingListForm()
        return response
