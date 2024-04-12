from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProfiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)
    
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in = skills))
    return profiles, search_query

def paginateProject(request, profiles, results):
    page = request.GET.get('page')
    result = 3
    paginator = Paginator(profiles, result)
    
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:  # Makes sure that your first page does not start with a numer
        page = 1;
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
         
    #Rolling window for page
    leftindex = (int(page)-1)
    if leftindex < 1:
        leftindex = 1
        
    rightindex = (int(page)+1)
    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages
        
    custom_range = range(leftindex, rightindex+1)
    return custom_range, profiles