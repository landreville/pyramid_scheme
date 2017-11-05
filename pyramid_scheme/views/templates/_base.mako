<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8"/>
        <title>
            pyramid_scheme
            ${ '— {}'.format(capture(self.title)) if capture(self.title) else '' }
        </title>
        <link rel="stylesheet" href="/static/css/bundle.css"/>
    </head>
    <body>
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
