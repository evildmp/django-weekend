# Django settings for example project.

import os.path
from sekrit_settings import *

# Make it work straight from the checkout!
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# set the BASE_PATH for convenience's sake
BASE_PATH = os.path.normpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (u'Daniele Procida', 'daniele@vurt.org'),
)

MANAGERS = ADMINS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'
DATE_FORMAT = "jS F Y"
TIME_FORMAT = "H\.i"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_PATH, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'legacy_finders.LegacyAppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    # 'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',

    "cms.context_processors.media",
    'sekizai.context_processors.sekizai',

    "arkestra_utilities.context_processors.arkestra_templates",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'djangoweekend.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

INSTALLED_APPS = (

     # Django CMS applications

    'arkestra_utilities',
    'cms',
    'menus',
    # 'appmedia',
    'cms.plugins.text',
    'cms.plugins.snippet',
    'sekizai',
    # 'djcelery',     # will need to be enabled for celery processing

    # Arkestra applications

    'contacts_and_people',
    'vacancies_and_studentships',
    'news_and_events',
    'links',
    'arkestra_utilities.widgets.combobox',
    'arkestra_image_plugin',
    'video',
    'housekeeping',

    # other applications

    'polymorphic',
    'semanticeditor',
    'mptt',
    'easy_thumbnails',
    'typogrify',
    'filer',
    'widgetry',
    # 'south', # don't leave this disabled
    'treeadmin',

    # core Django applications
    # these should be last, so we can override their templates

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.markup'
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

# ------------------------ Django Celery
try:
    import djcelery
    djcelery.setup_loader()

    BROKER_HOST = "localhost"
    BROKER_PORT = 5672
    BROKER_USER = "guest"
    BROKER_PASSWORD = "guest"
    BROKER_VHOST = "/"
except ImportError:
    pass


# ------------------------ Django Filer

FILER_FILE_MODELS = (
        'video.models.Video',
        'filer.models.imagemodels.Image',
        'filer.models.filemodels.File',
    )

# ------------------------ Django CMS

gettext = lambda s: s

CMS_SOFTROOT = True
CMS_PERMISSION = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True


# this is only here because I don't know how to make other apps find it otherwise, and they rely on it.
CMS_MEDIA_URL = STATIC_URL + 'cms/'

CMS_TEMPLATES = (
    ('institute.html', gettext('Institute of Mediaeval Medicine')),
    ('djangoweekend.html', gettext('Django Weekend')),
    ('djangoweekenddev.html', gettext('Django Weekend dev')),
)

CMS_PAGE_FLAGS = (
    ('no_local_menu', 'Hide local menu') ,
    ('no_horizontal_menu', 'No horizontal menu') ,
    ('no_page_title', "Don't display page title") ,
    )

CMS_PLACEHOLDER_CONF = {
    'body': {
        # "plugins": (
        #     'SemanticTextPlugin',
        #     'CMSVacanciesPlugin',
        #     'CMSNewsAndEventsPlugin',
        #     'SnippetPlugin',
        #     'LinksPlugin',
        #     'CMSPublicationsPlugin',
        #     'ImagePlugin',
        #     'ImageSetPublisher',
        #     'EntityAutoPageLinkPluginPublisher',
        #     'EntityMembersPluginPublisher',
        #     'FilerImagePlugin',
        #     'EntityDirectoryPluginPublisher',
        #     'CarouselPluginPublisher',
        #     'FocusOnPluginPublisher',
        #     'VideoPluginPublisher',
        #     ),
        "extra_context": {
            "width":"880",
            },
        "name": gettext("body"),
    },
}

LANGUAGES = (
('en', gettext('English')),
)

# ------------------------ WYMeditor/SemanticEditor

# these override the settings in cms.plugins.text.settings

WYM_TOOLS = ",\n".join([
    "{'name': 'Italic', 'title': 'Emphasis', 'css': 'wym_tools_emphasis'}",
    "{'name': 'Bold', 'title': 'Strong', 'css': 'wym_tools_strong'}",
    "{'name': 'InsertOrderedList', 'title': 'Ordered_List', 'css': 'wym_tools_ordered_list'}",
    "{'name': 'InsertUnorderedList', 'title': 'Unordered_List', 'css': 'wym_tools_unordered_list'}",
    "{'name': 'Indent', 'title': 'Indent', 'css': 'wym_tools_indent'}",
    "{'name': 'Outdent', 'title': 'Outdent', 'css': 'wym_tools_outdent'}",
    "{'name': 'Undo', 'title': 'Undo', 'css': 'wym_tools_undo'}",
    "{'name': 'Redo', 'title': 'Redo', 'css': 'wym_tools_redo'}",
    "{'name': 'ToggleHtml', 'title': 'HTML', 'css': 'wym_tools_html'}",
])

WYM_CONTAINERS = ",\n".join([
    "{'name': 'P', 'title': 'Paragraph', 'css': 'wym_containers_p'}",
   # "{'name': 'H1', 'title': 'Heading_1', 'css': 'wym_containers_h1'}", # I assume you reserve <h1> for your page templates
    "{'name': 'H2', 'title': 'Heading_2', 'css': 'wym_containers_h2'}",
    "{'name': 'H3', 'title': 'Heading_3', 'css': 'wym_containers_h3'}",
    "{'name': 'H4', 'title': 'Heading_4', 'css': 'wym_containers_h4'}",
    "{'name': 'H5', 'title': 'Heading_5', 'css': 'wym_containers_h5'}",
    "{'name': 'H6', 'title': 'Heading_6', 'css': 'wym_containers_h6'}",
#    "{'name': 'PRE', 'title': 'Preformatted', 'css': 'wym_containers_pre'}",
   "{'name': 'BLOCKQUOTE', 'title': 'Blockquote', 'css': 'wym_containers_blockquote'}",
   # "{'name': 'TH', 'title': 'Table_Header', 'css': 'wym_containers_th'}", # not ready for this yet
])

from arkestra_settings import *# import pdb; pdb.set_trace()
