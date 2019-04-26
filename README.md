# XjShop
基于django编写的一套framework api供前端调用, 参考教程, 目前正在施工中
├─.idea
│  └─inspectionProfiles
├─apps
│  ├─goods
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  └─__pycache__
│  ├─trade
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  └─__pycache__
│  ├─users
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  └─__pycache__
│  ├─user_operation
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  └─__pycache__
│  └─__pycache__
├─db_tools
│  ├─data
│  │  └─__pycache__
│  └─__pycache__
├─extra_apps
│  ├─DjangoUeditor
│  │  ├─static
│  │  │  └─ueditor
│  │  │      ├─dialogs
│  │  │      │  ├─anchor
│  │  │      │  ├─attachment
│  │  │      │  │  ├─fileTypeImages
│  │  │      │  │  └─images
│  │  │      │  ├─background
│  │  │      │  │  └─images
│  │  │      │  ├─charts
│  │  │      │  │  └─images
│  │  │      │  ├─emotion
│  │  │      │  │  └─images
│  │  │      │  ├─gmap
│  │  │      │  ├─help
│  │  │      │  ├─image
│  │  │      │  │  └─images
│  │  │      │  ├─insertframe
│  │  │      │  ├─link
│  │  │      │  ├─map
│  │  │      │  ├─music
│  │  │      │  ├─preview
│  │  │      │  ├─scrawl
│  │  │      │  │  └─images
│  │  │      │  ├─searchreplace
│  │  │      │  ├─snapscreen
│  │  │      │  ├─spechars
│  │  │      │  ├─table
│  │  │      │  ├─template
│  │  │      │  │  └─images
│  │  │      │  ├─video
│  │  │      │  │  └─images
│  │  │      │  ├─webapp
│  │  │      │  └─wordimage
│  │  │      ├─lang
│  │  │      │  ├─en
│  │  │      │  │  └─images
│  │  │      │  └─zh-cn
│  │  │      │      └─images
│  │  │      ├─php
│  │  │      ├─themes
│  │  │      │  └─default
│  │  │      │      ├─css
│  │  │      │      └─images
│  │  │      ├─third-party
│  │  │      │  ├─codemirror
│  │  │      │  ├─highcharts
│  │  │      │  │  ├─adapters
│  │  │      │  │  ├─modules
│  │  │      │  │  └─themes
│  │  │      │  ├─snapscreen
│  │  │      │  ├─SyntaxHighlighter
│  │  │      │  ├─video-js
│  │  │      │  │  └─font
│  │  │      │  ├─webuploader
│  │  │      │  └─zeroclipboard
│  │  │      └─_examples
│  │  │          └─server
│  │  ├─templates
│  │  └─__pycache__
│  ├─xadmin
│  │  ├─.tx
│  │  ├─locale
│  │  │  ├─de_DE
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─en
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─es_MX
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─eu
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─id_ID
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─ja
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─lt
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─nl_NL
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─pl
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─pt_BR
│  │  │  │  └─LC_MESSAGES
│  │  │  ├─ru_RU
│  │  │  │  └─LC_MESSAGES
│  │  │  └─zh_Hans
│  │  │      └─LC_MESSAGES
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  ├─plugins
│  │  │  └─__pycache__
│  │  ├─static
│  │  │  └─xadmin
│  │  │      ├─css
│  │  │      │  └─themes
│  │  │      ├─js
│  │  │      └─vendor
│  │  │          ├─autotype
│  │  │          ├─bootstrap
│  │  │          │  ├─css
│  │  │          │  ├─fonts
│  │  │          │  └─js
│  │  │          ├─bootstrap-clockpicker
│  │  │          ├─bootstrap-datepicker
│  │  │          │  ├─css
│  │  │          │  └─js
│  │  │          │      └─locales
│  │  │          ├─bootstrap-image-gallery
│  │  │          │  ├─css
│  │  │          │  ├─img
│  │  │          │  └─js
│  │  │          ├─bootstrap-modal
│  │  │          │  ├─css
│  │  │          │  ├─img
│  │  │          │  └─js
│  │  │          ├─bootstrap-multiselect
│  │  │          │  ├─css
│  │  │          │  └─js
│  │  │          ├─bootstrap-timepicker
│  │  │          │  ├─css
│  │  │          │  └─js
│  │  │          ├─flot
│  │  │          ├─font-awesome
│  │  │          │  ├─css
│  │  │          │  └─fonts
│  │  │          ├─jquery
│  │  │          ├─jquery-ui
│  │  │          ├─load-image
│  │  │          ├─select2
│  │  │          ├─selectize
│  │  │          └─snapjs
│  │  ├─templates
│  │  │  └─xadmin
│  │  │      ├─auth
│  │  │      │  ├─password_reset
│  │  │      │  └─user
│  │  │      ├─blocks
│  │  │      ├─edit_inline
│  │  │      ├─filters
│  │  │      ├─forms
│  │  │      ├─grids
│  │  │      ├─import_export
│  │  │      ├─includes
│  │  │      ├─layout
│  │  │      ├─views
│  │  │      └─widgets
│  │  ├─templatetags
│  │  │  └─__pycache__
│  │  ├─views
│  │  │  └─__pycache__
│  │  └─__pycache__
│  └─__pycache__
├─media
│  ├─banner
│  ├─brands
│  ├─goods
│  │  └─images
│  └─message
│      └─images
├─templates
└─XjShop
    └─__pycache__
