
<form class="form" method="POST">
    <div class="form__group">
        <label class="form__label">
            Username:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="username"
                value="${form_value(request, user, 'username')}"/>

            % if form_errors and form_errors.get('username'):
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
                value="${form_value(request, user, 'first_name')}"/>

            % if form_errors and form_errors.get('first_name'):
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
                value="${form_value(request, user, 'last_name')}"/>

            % if form_errors and form_errors.get('last_name'):
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
                value="${form_value(request, user, 'email')}"/>

            % if form_errors and form_errors.get('email'):
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
