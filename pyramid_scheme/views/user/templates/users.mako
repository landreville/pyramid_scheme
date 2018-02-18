<%inherit file="/_base.mako"/>

<%block name="title">Users</%block>
<table>
    <thead>
        <tr>
            <th>Username</th>
            <th>First name</th>
            <th>Last name</th>
            <th>Email</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        % for user, view_link in users:
            <tr>
                <td>${user.username}</td>
                <td>${user.first_name}</td>
                <td>${user.last_name}</td>
                <td>${user.email}</td>
                <td>
                    <a class="button-nav" href="${view_link}">View</a>
                </td>
            </tr>
        % endfor
    </tbody>
</table>
