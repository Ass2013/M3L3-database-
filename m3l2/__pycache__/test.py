        connection.execute('''
    INSERT INTO projects VALUES
    (1, 1, 'Final Project of python level 2', 'A project that explains about polution, there are also 2 fun quizes', 'https://github.com/Ass2013/save-human-kind-from-diying.git', 2),
    (2, 2, 'Eco Dom Calculator', 'A project that calculates the efficiency of a building', 'https://github.com/Ass2013/eco-dom-calculator.git', 3),
        3, 3, 'First Flask Project', 'A project in which i learned how  to use flask', 'https://github.com/Ass2013/flassk-project.git', 4)
''')
        connection.commit()
        connection.execute('''
    INSERT INTO status VALUES
        (1, 'Not Started'),
        (2, 'In Progress'),
        (3, 'Completed'),
        (4, 'On Hold'))
''')
        connection.commit()
        connection.execute('''
    INSERT INTO skills VALUES
        (1, 'Python'),
        (2, 'JavaScript'),
        (3, 'SQL'),
        (4, 'HTML/CSS'),
        (5, 'Flask'))
''')
        connection.commit()
        connection.execute('''
    INSERT INTO project_skills VALUES
        (1, 1),
        (1, 5),
        (2, 3),
        (2, 4),
        (3, 5))
''')
        connection.commit()