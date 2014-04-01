from django.conf.urls import patterns, include, url
from account.views import SignUpView, userlogin


urlpatterns = patterns('account.views',
    # Examples:
    # url(r'^$', 'p1.views.home', name='home'),
    # url(r'^p1/', include('p1.foo.urls')),
    #url(r'^newpoll$', 'newpoll'),
    #url(r'^$', 'polls'),  
    #function based url  url(r'^signup$', 'sign_up'), 
    #class based urls
    url(r'^signup$', SignUpView.as_view(), name='Sign_up'),
   
    url(r'^login$', userlogin),



   

    
)

