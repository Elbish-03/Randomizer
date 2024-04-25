function divideNames() {
    var namesTextarea = document.getElementById('namesTextarea');
    var rolesTextarea = document.getElementById('rolesTextarea');
    var names = namesTextarea.value.split(',').map(name => name.trim());
    var roles = rolesTextarea.value.split(',').map(role => role.trim());

    var numGroupsInput = document.getElementById('numGroupsInput');
    var numGroups = parseInt(numGroupsInput.value);

    var groupsContainer = document.getElementById('groupsContainer');
    groupsContainer.innerHTML = '';

    var groups = [];
    for (var i = 0; i < numGroups; i++) {
        groups.push({ names: [], roles: [] });
    }

    var groupIndex = 0;
    for (var i = 0; i < names.length; i++) {
        groups[groupIndex].names.push(names[i]);
        groupIndex = (groupIndex + 1) % numGroups;
    }

    groupIndex = 0;
    for (var i = 0; i < roles.length; i++) {
        groups[groupIndex].roles.push(roles[i]);
        groupIndex = (groupIndex + 1) % numGroups;
    }

    // Display groups
    var groupsOutput = document.getElementById('groupsOutput');
    groupsOutput.style.display = 'block';

    groups.forEach(function(group, index) {
        var groupTable = document.createElement('table');
        groupTable.classList.add('group-table');

        var groupCaption = document.createElement('caption');
        groupCaption.textContent = 'Group ' + (index + 1);
        groupTable.appendChild(groupCaption);

        var namesRow = document.createElement('tr');
        var namesHeader = document.createElement('th');
        namesHeader.textContent = 'Names:';
        namesRow.appendChild(namesHeader);
        group.names.forEach(function(name) {
            var nameCell = document.createElement('td');
            nameCell.textContent = name;
            namesRow.appendChild(nameCell);
        });
        groupTable.appendChild(namesRow);

        var rolesRow = document.createElement('tr');
        var rolesHeader = document.createElement('th');
        rolesHeader.textContent = 'Roles:';
        rolesRow.appendChild(rolesHeader);
        group.roles.forEach(function(role) {
            var roleCell = document.createElement('td');
            roleCell.textContent = role;
            rolesRow.appendChild(roleCell);
        });
        groupTable.appendChild(rolesRow);

        groupsContainer.appendChild(groupTable);
    });
}
