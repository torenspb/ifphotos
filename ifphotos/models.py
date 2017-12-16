from django.db import models

# Collecting every visitor's REQUEST_METHOD, REMOTE_ADDR,
# HTTP_USER_AGENT and POST search value from http request


class Visitor(models.Model):

    datetime = models.DateTimeField(auto_now=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=100, blank=True)
    req_method = models.CharField(max_length=1, default=0)
    search_value = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.id)
