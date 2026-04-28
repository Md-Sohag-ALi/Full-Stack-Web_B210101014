const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("task-list");
const todoInput = document.getElementById("todo-input");

const formSubmitHandler = (event) => {
  event.preventDefault();

  const inputText = todoInput.value;

  // create proper task UI
  const task = `
    <div class="flex items-center justify-between bg-gray-50 p-3 rounded-lg">
      <div class="flex items-center gap-2">
        <input type="checkbox" class="accent-purple-600">
        <span class="text-sm">${inputText}</span>
      </div>
      <button class="text-gray-400 hover:text-red-500">🗑</button>
    </div>
  `;

  // add new task on top
  todoList.innerHTML = task + todoList.innerHTML;

  // clear input
 todoInput.value = "";
};

todoForm.addEventListener("submit", formSubmitHandler);