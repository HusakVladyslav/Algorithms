import networkx as nx
import matplotlib.pyplot as plt
import instaloader

# Завантаження підписників з Instagram API
def get_followers(username, password):
    L = instaloader.Instaloader()
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, username)
    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)
    return followers

# Створення графа
def create_graph(username, password):
    followers = get_followers(username, password)
    G = nx.Graph()
    for follower in followers:
        G.add_edge(username, follower)
    return G

# Візуалізація графа
def visualize_graph(G):
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color='red', node_size=1000, edge_color='gray', linewidths=1, font_size=12)
    plt.title("Граф підписників на Instagram")
    plt.show()

# Обчислення діаметру графа
def calculate_diameter(G):
    diameter = nx.diameter(G)
    print("Діаметр графа:", diameter)

# Змініть username та password на свої дані в Instagram
username = "username"
password = "password"

# Створення графа
G = create_graph(username, password)

# Збереження графа у форматі GraphML
nx.write_graphml(G, "instagram_graph.graphml")

# Виведення повідомлення про успішне збереження
print("Граф збережено у файл 'instagram_graph.graphml'")

# Візуалізація графа
visualize_graph(G)

# Обчислення діаметру графа
calculate_diameter(G)

