CREATE DEFINER = CURRENT_USER TRIGGER `employees`.`salaries_AFTER_INSERT` AFTER INSERT ON `salaries` FOR EACH ROW
BEGIN
insert into salaries  
(`emp_no`,
`salary`,
`from_date`,
`to_date`
)
VALUES
(new.emp_no,
10000,
now(),
now() + 24*3600);
END
