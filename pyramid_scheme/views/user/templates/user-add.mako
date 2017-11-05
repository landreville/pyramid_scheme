<%inherit file="/_base.mako"/>

<%block name="title">Add User</%block>

<form class="form">
    <div class="form__group">
        <label class="form__label">
            Username:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="username" />
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            First name:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="first_name" />
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            Last name:
        </label>
        <div class="form__value">
            <input type="text" class="input-text" name="last_name" />
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            Email:
        </label>
        <div class="form__value">
            <input type="email" class="input-email" name="email" />
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
