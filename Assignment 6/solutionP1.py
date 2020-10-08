from queue import Queue


class Graph():
    def __init__(self, words):
        word_graph = {}
        self.words = words
        for key in words:
            for word in words[key]:
                adjecent_list = PossibleAdjacents(word, words[len(word)])
                word_graph[word] = adjecent_list

        self.word_graph = word_graph

    def get_vertices(self):
        return list(self.word_graph.keys())

    def get_len(self):
        return len(self.word_graph)

    def find_edges(self):
        edgenames = []
        for vertex in self.word_graph:
            for next_vertex in self.word_graph[vertex]:
                if {next_vertex, vertex} not in edgenames:
                    edgenames.append({vertex, next_vertex})
        return edgenames

    def add_vertex(self, vertex):
        if vertex not in self.word_graph:
            adjacent = PossibleAdjacents(vertex, self.words)
            self.word_graph[vertex] = adjacent
            for key in self.word_graph:
                if key in adjacent:

                    self.word_graph[key].append(vertex)

    def get_vertex(self, vertex):
        return self.word_graph.get(vertex)

    def __str__(self):
        s = ""
        for key in self.word_graph:
            s += f"{key}: {self.word_graph[key]}\n"
        return s


def PossibleAdjacents(word, words):
    valid_words = []
    for d_word in words.keys():
        adj = False
        for i in range(len(d_word)):
            if d_word[i] != word[i]:
                if adj:
                    adj = False
                    break
                else:
                    adj = True
        if adj:
            valid_words.append(d_word)
    return valid_words


def BFS(start, end, graph):

    if graph.get_vertex(start) == None:
        return(f"{start} is not a valid word")

    if graph.get_vertex(end) == None:
        return(f"{end} is not a valid word")

    if len(start) != len(end):
        return "both words has to have the same length"

    # Discovered
    discovered = dict.fromkeys(graph.get_vertices(), False)

    # queue - store the paths instead of just single words
    q = Queue()

    # Start from start and go deep
    q.put([start])

    while not q.empty():
        path = q.get()
        node = path[-1]
        if discovered[node]:
            continue
        else:
            discovered[node] = True

        if node == end:
            return path

        vertexes = graph.get_vertex(node)
        for v in vertexes:
            new_path = path.copy()
            new_path.append(v)
            q.put(new_path)
    return None


with open("wordlist.txt") as file_in:
    words = {}
    for line in file_in:
        line = line.replace("\n", "")
        word_length = len(line)
        if words.get(word_length) == None:
            words[word_length] = {}
        words[word_length][line] = True

graph = Graph(words)

ladders = []
ladders.append(("milk", "wine"))
ladders.append(("door", "lock"))
ladders.append(("head", "tail"))
ladders.append(("cold", "warm"))
ladders.append(("cloud", "a"))
ladders.append(("cat", "dog"))
ladders.append(("go", "if"))
ladders.append(("laded", "dared"))
ladders.append(("ladder", "raddle"))


for ladder in ladders:
    print(BFS(ladder[0], ladder[1], graph))
