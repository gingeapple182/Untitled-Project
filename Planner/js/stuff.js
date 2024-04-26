var tasks = [];
var tasksRemaining = 0;

function addTask() {
    var taskInput = document.getElementById("taskInput");
    var priorityInput =  document.getElementById("priorityselect");
    var taskText = taskInput.value.trim();
    var priority = prioritySelect.value;

    if (taskText !== " ") {
        var newTask = {
            name: taskText,
            priority: priority
        };
        tasks.push(newTask);
        displayTasks();
        taskInput.value = " ";
        prioritySelect.selectedIndex = 0;
        updateTaskCount();
    }
}

function removeTask(index) {
    tasks.splice(index, 1);
    displayTasks();
    updateTaskCount();
}

function displayTasks() {
    var taskList = document.getElementById("tasks");
    taskList.innerHTML = "";

    tasks.forEach(function(task, index) {
        var listItem = document.createElement("li");
        listItem.textContent = `${task.name} (Priority: ${task.priority})`;

        var removeButton = document.createElement("button");
        removeButton.textContent = "Complete";
        removeButton.onclick = function() {
            removeTask(index);
        };

        listItem.appendChild(removeButton);
        taskList.appendChild(listItem);
    });
}

function updateTaskCount() {
    tasksRemaining = tasks.length;
    document.getElementById("tasksRemaining").textContent = tasksRemaining;
}
