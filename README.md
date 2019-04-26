<!DOCTYPE html><html><head><title>XjShop</title><meta charset='utf-8'><link href='https://cdn.maxiang.io/res-min/themes/marxico.css' rel='stylesheet'><style></style></head><body><div id='preview-contents' class='note-content'>
                        
                    

<h1 id="xjshop">XjShop</h1>

<p>基于django编写的一套framework api供前端调用, 参考教程, 目前正在施工中 <br>
├─.idea <br>
│  └─inspectionProfiles <br>
├─apps <br>
│  ├─goods <br>
│  │  ├─migrations <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  └─<strong>pycache</strong> <br>
│  ├─trade <br>
│  │  ├─migrations <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  └─<strong>pycache</strong> <br>
│  ├─users <br>
│  │  ├─migrations <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  └─<strong>pycache</strong> <br>
│  ├─user_operation <br>
│  │  ├─migrations <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  └─<strong>pycache</strong> <br>
│  └─<strong>pycache</strong> <br>
├─db_tools <br>
│  ├─data <br>
│  │  └─<strong>pycache</strong> <br>
│  └─<strong>pycache</strong> <br>
├─extra_apps <br>
│  ├─DjangoUeditor <br>
│  │  ├─static <br>
│  │  │  └─ueditor <br>
│  │  │      ├─dialogs <br>
│  │  │      │  ├─anchor <br>
│  │  │      │  ├─attachment <br>
│  │  │      │  │  ├─fileTypeImages <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─background <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─charts <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─emotion <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─gmap <br>
│  │  │      │  ├─help <br>
│  │  │      │  ├─image <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─insertframe <br>
│  │  │      │  ├─link <br>
│  │  │      │  ├─map <br>
│  │  │      │  ├─music <br>
│  │  │      │  ├─preview <br>
│  │  │      │  ├─scrawl <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─searchreplace <br>
│  │  │      │  ├─snapscreen <br>
│  │  │      │  ├─spechars <br>
│  │  │      │  ├─table <br>
│  │  │      │  ├─template <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─video <br>
│  │  │      │  │  └─images <br>
│  │  │      │  ├─webapp <br>
│  │  │      │  └─wordimage <br>
│  │  │      ├─lang <br>
│  │  │      │  ├─en <br>
│  │  │      │  │  └─images <br>
│  │  │      │  └─zh-cn <br>
│  │  │      │      └─images <br>
│  │  │      ├─php <br>
│  │  │      ├─themes <br>
│  │  │      │  └─default <br>
│  │  │      │      ├─css <br>
│  │  │      │      └─images <br>
│  │  │      ├─third-party <br>
│  │  │      │  ├─codemirror <br>
│  │  │      │  ├─highcharts <br>
│  │  │      │  │  ├─adapters <br>
│  │  │      │  │  ├─modules <br>
│  │  │      │  │  └─themes <br>
│  │  │      │  ├─snapscreen <br>
│  │  │      │  ├─SyntaxHighlighter <br>
│  │  │      │  ├─video-js <br>
│  │  │      │  │  └─font <br>
│  │  │      │  ├─webuploader <br>
│  │  │      │  └─zeroclipboard <br>
│  │  │      └─_examples <br>
│  │  │          └─server <br>
│  │  ├─templates <br>
│  │  └─<strong>pycache</strong> <br>
│  ├─xadmin <br>
│  │  ├─.tx <br>
│  │  ├─locale <br>
│  │  │  ├─de_DE <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─en <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─es_MX <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─eu <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─id_ID <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─ja <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─lt <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─nl_NL <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─pl <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─pt_BR <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  ├─ru_RU <br>
│  │  │  │  └─LC_MESSAGES <br>
│  │  │  └─zh_Hans <br>
│  │  │      └─LC_MESSAGES <br>
│  │  ├─migrations <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  ├─plugins <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  ├─static <br>
│  │  │  └─xadmin <br>
│  │  │      ├─css <br>
│  │  │      │  └─themes <br>
│  │  │      ├─js <br>
│  │  │      └─vendor <br>
│  │  │          ├─autotype <br>
│  │  │          ├─bootstrap <br>
│  │  │          │  ├─css <br>
│  │  │          │  ├─fonts <br>
│  │  │          │  └─js <br>
│  │  │          ├─bootstrap-clockpicker <br>
│  │  │          ├─bootstrap-datepicker <br>
│  │  │          │  ├─css <br>
│  │  │          │  └─js <br>
│  │  │          │      └─locales <br>
│  │  │          ├─bootstrap-image-gallery <br>
│  │  │          │  ├─css <br>
│  │  │          │  ├─img <br>
│  │  │          │  └─js <br>
│  │  │          ├─bootstrap-modal <br>
│  │  │          │  ├─css <br>
│  │  │          │  ├─img <br>
│  │  │          │  └─js <br>
│  │  │          ├─bootstrap-multiselect <br>
│  │  │          │  ├─css <br>
│  │  │          │  └─js <br>
│  │  │          ├─bootstrap-timepicker <br>
│  │  │          │  ├─css <br>
│  │  │          │  └─js <br>
│  │  │          ├─flot <br>
│  │  │          ├─font-awesome <br>
│  │  │          │  ├─css <br>
│  │  │          │  └─fonts <br>
│  │  │          ├─jquery <br>
│  │  │          ├─jquery-ui <br>
│  │  │          ├─load-image <br>
│  │  │          ├─select2 <br>
│  │  │          ├─selectize <br>
│  │  │          └─snapjs <br>
│  │  ├─templates <br>
│  │  │  └─xadmin <br>
│  │  │      ├─auth <br>
│  │  │      │  ├─password_reset <br>
│  │  │      │  └─user <br>
│  │  │      ├─blocks <br>
│  │  │      ├─edit_inline <br>
│  │  │      ├─filters <br>
│  │  │      ├─forms <br>
│  │  │      ├─grids <br>
│  │  │      ├─import_export <br>
│  │  │      ├─includes <br>
│  │  │      ├─layout <br>
│  │  │      ├─views <br>
│  │  │      └─widgets <br>
│  │  ├─templatetags <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  ├─views <br>
│  │  │  └─<strong>pycache</strong> <br>
│  │  └─<strong>pycache</strong> <br>
│  └─<strong>pycache</strong> <br>
├─media <br>
│  ├─banner <br>
│  ├─brands <br>
│  ├─goods <br>
│  │  └─images <br>
│  └─message <br>
│      └─images <br>
├─templates <br>
└─XjShop <br>
    └─<strong>pycache</strong></p></div></body></html>
