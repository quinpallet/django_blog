from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blog1'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのIndexVieを実行
    # URLパターン名は'index'
    path('', views.IndexView.as_view(), name='index'),

    # リクエストされたURLが「blog-detal/レコードのid/」の場合
    # viewsモジュールのBlogDetalを実行
    # URLパターン名は'blog_detail'
    path(
        # 詳細ページのURLは「blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターンの名前を'blog_detail'にする
        name='blog_detail'
        ),
    path(
        # scienceカテゴリの一覧ページのURLは「science-list/」
        'science-list/',
        # viewsモジュールのScienceViewを実行
        views.ScienceView.as_view(),
        # URLパターンの名前を'science_list'にする
        name='science_list'
        ),
    path(
        # dailylistカテゴリの一覧ページのURLは「dailylist-list/」
        'dailylist-list/',
        # viewsモジュールのScienceViewを実行
        views.DailylifeView.as_view(),
        # URLパターンの名前を'dailylist_list'にする
        name='dailylife_list'
        ),
    path(
        # musicカテゴリの一覧ページのURLは「music-list/」
        'music-list/',
        # viewsモジュールのMusicViewを実行
        views.MusicView.as_view(),
        # URLパターンの名前を'music_list'にする
        name='music_list'
        ),
]
