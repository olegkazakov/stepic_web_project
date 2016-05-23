from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from qa.views import test, list, popular, question_detail
from qa.views import question_ask, question_answer
from qa.views import user_signup, user_login, user_logout

urlpatterns = [
    url(r'^$', list, name='list'),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^popular/', popular, name='popular'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^login/', user_login, name='login'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^logout/', user_login, name='logout'),
    url(r'^new/', test, name='new')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)