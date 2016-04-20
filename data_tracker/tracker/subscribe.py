from django.core.mail import send_mail
#from tracker.models import Tracker
from datetime import datetime
from django.contrib.auth.models import Group

admin = 'lua1@email.chop.edu' #change to cbttc.cbio@gmail.com after testing

class Subscribe:
    def notify(self):
        unsubscribe =  '<a href ="/tracker/unsubscribe">Unsubscribe</a>' # Need to ecape and mark_safe html in body
        ### Subscription selections
        if (self.subscription > 0):
            if self.subscription == 1:
                available_group = Group.objects.get(name='available')
                if self.trackerID == 4:
                    # Send CbioPortal email with link to cbio
                    body = 'Data Tracker Request Available in cBioPortal+ \n\n'
                    for property, value in vars(latest_obj).iteritems():
                        #TODO filter out irrelevant _state info
                        body = body + property + ": " + str(value) + '\n'
                    body = body + unsubscribe
                    email = EmailMessage('Data Tracker Request Available', body, to=[available_list])
                    email.send()
                elif self.trackerID == 5:
                    # Send Cavatica email with link
                    body = 'Data Tracker Request Available in Cavatica \n\n'
                    for property, value in vars(latest_obj).iteritems():
                        body = body + property + ": " + str(value) + '\n'
                    email = EmailMessage('Data Tracker Request Available', body, to=[available_list])
                    email.send()
            elif self.subscription == 2:
                # Send an email showing what step the request is at
                # TODO insert a custom tracker steps view here (check if html will show in SMTP's body)
                body = 'Your Data Tracker Request has been updated to a new step. \n\n'
                for property, value in vars(latest_obj).iteritems():
                    body = body + property + ": " + str(value) + '\n'
                email = EmailMessage('Data Tracker Request Available', body, to=[step_list])
                email.send()
        elif(self.subscription > 2):
            # Email the admin an error because the subscription choices must be within 0 - 2
            body = 'The following request subscription choice is out of range. \n\n'
            for property, value in vars(latest_obj).iteritems():
                body = body + property + ": " + str(value) + '\n'
            email = EmailMessage('Data Tracker Subscription Error', body, to=[admin])
            email.send()

### TODO Time based polling

#def summary(self):
#    return self;
# Send me a weekly summary of new tracker items added that week

# Send me a monthly summary of new tracker items added that week
