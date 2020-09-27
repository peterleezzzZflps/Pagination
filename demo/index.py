from Pagination.page import Pagination

# query_set = models.Issues.objects.filter(project_id=project_id).filter(**condition) 你要查询所有的数据

page_obj = Pagination(
    current_page=request.GET.get("page"),  # 获取当前的页码数
    total_count=query_set.count(),  # 获取数据库中取到的所有数据的总数
    base_url=request.path_info,  # 获取页面的url
    params=request.GET,  # 获取整个页面的数据
    per_page_count=5  # 每页数据的个数
)

#   issues_obj_list = query_set[page_obj.start: page_obj.end]  获得分页后的数据
