<%doc>
    This is the base template to provide the HTML boiler plate for
    all pages. This will also render the site header and footer.
</%doc>
## Indicates page uses HTML5 content
<!doctype html>
## This page is written in english.
<html lang="en">
    <head>
        ## The page may include utf-8 characters.
        ## The title below even contains one in this code.
        <meta charset="utf-8"/>
        <link rel="stylesheet"
              href="${request.static_path('pyramid_scheme:static/css/bundle.css')}"/>
        <title>
            pyramid_scheme
            ## Use capture function to allow the title to be rendered in the
            ## title block below.
            ${ '— {}'.format(capture(self.title)) if capture(self.title) else '' }
        </title>
    </head>
    <body>

        ## Include the page title here to ensure each page renders the page title
        ## consistently.
        <div class="page-title">
            <h1 class="page-title__heading">
                <span class="page-title__text">
                    <%block name="title"/>
                </span>
            </h1>
        </div>

        <div class="content">
            ${next.body()}
        </div>
    </body>
</html>
