<%inherit file="/_base.mako"/>

<%block name="title">Add User</%block>

<form class="form" method="POST">
    <div class="form__group">
        <label class="form__label">
            Username:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="username"
                value="${request.params.get('username', '')}"/>

            % if form_errors and form_errors['username']:
                <div class="form__validation">
                    ${form_errors['username']}
                </div>
            % endif

        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            First name:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="first_name"
                value="${request.params.get('first_name', '')}"/>

            % if form_errors and form_errors['first_name']:
                <div class="form__validation">
                    ${form_errors['first_name']}
                </div>
            % endif

        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            Last name:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="last_name"
                value="${request.params.get('last_name', '')}"/>

            % if form_errors and form_errors['last_name']:
                <div class="form__validation">
                    ${form_errors['last_name']}
                </div>
            % endif

        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            Email:
        </label>
        <div class="form__value">
            <input type="email" class="input-email" name="email"
                value="${request.params.get('email', '')}"/>

            % if form_errors and form_errors['email']:
                <div class="form__validation">
                    ${form_errors['email']}
                </div>
            % endif

        </div>
    </div>
    <div class="form__group">
        <label class="form__label">

        </label>
        <div class="form__value">
            <button type="submit">Save</button>
        </div>
    </div>
</form>
