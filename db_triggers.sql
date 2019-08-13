#  Workbench тоже вылетает на триггерах. Возможно будет такое решение:

CREATE DEFINER = CURRENT_USER TRIGGER `employees`.`salaries_AFTER_INSERT` AFTER INSERT ON `salaries` FOR EACH ROW
BEGIN
insert into salaries set salaries.emp_no = new emp_no, salaries.salary=10000
END
