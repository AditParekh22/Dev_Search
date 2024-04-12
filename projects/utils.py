from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProjects(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)
    
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query) | 
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
        
    )  
    
    return projects, search_query

def paginateProject(request, projects, results):
    page = request.GET.get('page')
    result = 3
    paginator = Paginator(projects, result)
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:  # Makes sure that your first page does not start with a numer
        page = 1;
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
         
    #Rolling window for page
    leftindex = (int(page)-1)
    if leftindex < 1:
        leftindex = 1
        
    rightindex = (int(page)+1)
    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages
        
    custom_range = range(leftindex, rightindex+1)
    return custom_range, projects