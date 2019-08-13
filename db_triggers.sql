#  Workbench тоже вылетает на триггерах. Возможно будет такое решение:

CREATE DEFINER = CURRENT_USER TRIGGER `employees`.`salaries_AFTER_INSERT` AFTER INSERT ON `salaries` FOR EACH ROW
BEGIN
insert into salaries set as sl
('sl'.`emp_no`,
'sl'.`salary`,
'sl'.`from_date`,
'sl'.`to_date`
)
VALUES
(new.emp_no,
10000,
current timestamp,
current timestamp + 24*3600)
END
