def add_task(task_dict, new_task):
	task_dict[new_task['id']] = new_task
	return task_dict

def complete_task(task_dict, task_id):
    if task_id in task_dict:
        task_dict[task_id]['completed'] = True
    return task_dict
