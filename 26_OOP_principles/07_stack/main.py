
class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return '; '.join(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def contain(self, item):
        for each in self.stack:
            if item == each:
                return True
        return False

    def delete(self, item):
        self.stack.remove(item)

    def __len__(self):
        return len(self.stack)


class TaskManager:

    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for p in sorted(self.task.keys()):
                display.append('{} {}\n'.format(str(p), str(self.task[p])))
        return ''.join(display)

    def new_task(self, task, priority):
        for key, value in self.task.items():
            if self.task[key].contain(task):
                print('Error! The same task already exists. Task wasnt add in todo list.')
                return 0
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

    def delete_task(self, task):
        for key, value in self.task.items():
            if self.task[key].contain(task):
                self.task[key].delete(task)
            if len(self.task[key]) == 0:
                del self.task[key]
                break
        print('Error! Task list doesnt have this task.')


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("поесть", 4)
manager.new_task("сдать дз", 2)
print(manager)

# ### Some simple tests for deleting tasks and handling duplicates

# trying to delete task in priority with several items
manager.delete_task('сдать дз')
print()
print(manager)

# trying to delete task in priority with only one item
manager.delete_task('поесть')
print()
print(manager)

# trying to add duplicate
manager.new_task("сделать уборку", 0)
print()
print(manager)

# trying to delete task which doesnt represent in task list
manager.delete_task('хахаха')
print()
print(manager)
