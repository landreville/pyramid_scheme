<%inherit file="/_base.mako"/>

<%block name="title">User — ${user.username}</%block>

<div class="form form--readonly">
    <div class="form__group">
        <label class="form__label">
            Username:
        </label>
        <div class="form__value">
            ${user.username}
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            First name:
        </label>
        <div class="form__value">
            ${user.first_name}
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            Last name:
        </label>
        <div class="form__value">
            ${user.last_name}
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">
            Email:
        </label>
        <div class="form__value">
            ${user.email}
        </div>
    </div>
    <div class="form__group">
        <label class="form__label">

        </label>
        <div class="form__value">
            ## TODO: Add link to edit view
            <a class="button-nav" href="">
                Edit
            </a>
        </div>
    </div>
</div>
