# PACKAGES
import pandas as pd

# FRIEND SWIPING DATA
friend_swiping_data = {
    'name': ['Alex', 'Taylor', 'Jordan', 'Morgan', 'Chris'],
    'age': [25, 22, 28, 24, 30],
    'bio': [
        "Loves hiking and the outdoors.",
        "Avid reader and aspiring writer.",
        "Tech enthusiast and gamer.",
        "Foodie and world traveler.",
        "Music producer and DJ."
    ],
    'img': [
        "https://randomuser.me/api/portraits/men/10.jpg",
        "https://randomuser.me/api/portraits/women/21.jpg",
        "https://randomuser.me/api/portraits/men/33.jpg",
        "https://randomuser.me/api/portraits/women/45.jpg",
        "https://randomuser.me/api/portraits/men/67.jpg"
    ]
}

friend_swiping_df = pd.DataFrame(friend_swiping_data)

# OTHER DATA
data = {
    '0_degree': [
        'Alice', 'Bob', 'Charlie', 'Diana',
        'Emma', 'Frank', 'Grace', 'Henry',
        'Isabel', 'Jack', 'Kelly', 'Liam',
        'Maya', 'Noah', 'Olivia', 'Paul',
        'Quinn', 'Ryan', 'Sofia', 'Tyler',
        'Uma', 'Victor', 'Wendy', 'Xavier',
        'No', 'Liza', 'Karen', 'Ye',
        'Barbara', 'Kayleigh', 'Aideen'
    ],
    '1_degree': [
        {'Ivanka'},
        {'Alice', 'Diana'},
        {'Alice', 'Diana', 'Bob'},
        {'Alice', 'Bob'},
        {'Grace', 'Frank', 'Henry'},
        {'Emma', 'Grace', 'Henry'},
        {'Emma', 'Los', 'Isabel'},
        {'Frank', 'Grace', 'Jack'},
        {'Grace', 'Henry', 'Kelly'},
        {'Henry', 'Kelly', 'Liam'},
        {'Isabel', 'Jack', 'Maya'},
        {'Jack', 'Kelly', 'Noah'},
        {'Kelly', 'Liam', 'Olivia'},
        {'Maya', 'Olivia', 'Paul'},
        {'Maya', 'Noah', 'Quinn'},
        {'Noah', 'Olivia', 'Ryan'},
        {'Paul', 'Ryan', 'Sofia'},
        {'Quinn', 'Sofia', 'Tyler'},
        {'Ryan', 'Tyler', 'Uma'},
        {'Sofia', 'Uma', 'Victor'},
        {'Tyler', 'Victor', 'Wendy'},
        {'Uma', 'Wendy', 'Xavier'},
        {'Victor', 'Xavier', 'Quinn'},
        {'Wendy', 'Uma', 'Ryan'},
        {'Liza', 'Karen'},
        {'No', 'Karen'},
        {'No'},
        set(),
        {'Kayleigh', 'Aideen'},
        {'Aideen', 'Barbara'},
        {'Barbara', 'Kayleigh'}
    ],
    'interests': [
        {'music', 'dance'},
        {'reading', 'travel'},
        {'yoga', 'music'},
        {'dance', 'reading'},
        {'yoga', 'travel'},
        {'music', 'yoga'},
        {'reading', 'travel'},
        {'music', 'dance'},
        {'yoga', 'reading'},
        {'travel', 'music'},
        {'dance', 'yoga'},
        {'music', 'reading', 'travel'},
        {'travel', 'yoga'},
        {'dance', 'music'},
        {'reading', 'yoga'},
        {'music', 'travel'},
        {'yoga', 'dance'},
        {'reading', 'travel', 'yoga'},
        {'music', 'dance'},
        {'travel', 'yoga'},
        {'yoga', 'music'},
        {'dance', 'reading'},
        {'music', 'yoga'},
        {'travel', 'dance'},
        {'reading'},
        {'music'},
        {'yoga'},
        {'travel'},
        {'travel'},
        {'music'},
        {'reading'}
    ],
    'activities': [
        {'sport', 'student gov'},
        {'sport', 'newspaper'},
        {'greek life', 'newspaper'},
        {'student gov', 'acapella'},
        {'sport', 'greek life'},
        {'newspaper', 'religious association'},
        {'sport', 'acapella'},
        {'student gov', 'newspaper'},
        {'acapella', 'religious association'},
        {'greek life', 'newspaper'},
        {'student gov', 'sport'},
        {'acapella', 'greek life'},
        {'sport', 'student gov'},
        {'greek life', 'newspaper'},
        {'sport', 'acapella'},
        {'student gov', 'religious association'},
        {'newspaper', 'sport'},
        {'acapella', 'student gov'},
        {'greek life', 'newspaper'},
        {'religious association', 'sport'},
        {'student gov', 'acapella'},
        {'greek life', 'sport'},
        {'newspaper', 'religious association'},
        {'sport', 'student gov'},
        {'acapella', 'religious association'},
        {'sport', 'newspaper'},
        {'acapella', 'student gov'},
        set(),
        {'sport'},
        {'greek life'},
        set()
    ]
}

df = pd.DataFrame(data)
