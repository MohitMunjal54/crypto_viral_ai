from data_collector import DataCollector
from analyzer import Analyzer
from generator import Generator

if __name__ == "__main__":

    print("Collecting data...")
    dc = DataCollector()
    collected = {
        "youtube": dc.fetch_youtube(),
        "twitter": dc.fetch_twitter(),
        "reddit": dc.fetch_reddit(),
        "news": dc.fetch_news()
    }

    print("Analyzing patterns...")
    az = Analyzer()
    patterns = az.find_patterns(collected)

    print("Generating ideas...")
    gen = Generator()
    ideas = gen.create_ideas(patterns)

    print("\n--- FINAL OUTPUT ---\n")
    print(ideas)
