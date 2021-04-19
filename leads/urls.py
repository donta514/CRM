from django.urls import path
from .views import ( 
    landing_page, contact_form, subscribe_form, info_form, LeadListView, 
    LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, 
    AssignAgentView, CategoryListView, CategoryDetailView, LeadCategoryUpdateView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail-view'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/category-detail/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    # path('signup/', signup_form, name='signup-form'),
    # path('login/', login_form, name='login-form'),
    path('home/', landing_page, name='landing-page'),
    path('contacts/', contact_form, name="contact-form"),
    path('subscribe/', subscribe_form, name="subscribe-form"),
    path('info/', info_form, name="info-form"),
    path('categories/', CategoryListView.as_view(), name="category-list")
]

