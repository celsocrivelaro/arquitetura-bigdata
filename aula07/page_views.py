from page_view_model import PageView
import faust

app = faust.App(
    'page_views',
    broker='kafka://kafka:9092'
)

page_view_topic = app.topic('page_views', value_type=PageView)
page_views = app.Table('page_views', default=int)

@app.agent(page_view_topic)
async def count_page_views(views):
    async for view in views.group_by(PageView.id):
        page_views[view.id] += 1

@app.page('/page_views/{page}')
@app.table_route(table=page_views, match_info='page')
async def get_count(web, request, page):
    return web.json({
        page: page_views[page],
    })