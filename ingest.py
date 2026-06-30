from src.ingestion.ingestion_pipeline import (
    IngestionPipeline
)


def main():

    print("\n" + "=" * 60)
    print("NeuroVLSI Knowledge Ingestion")
    print("=" * 60)

    pipeline = IngestionPipeline()

    try:

        total_chunks = pipeline.run()

        print("\n" + "=" * 60)
        print("Ingestion Completed")
        print("=" * 60)

        print(
            f"Total Chunks Indexed: "
            f"{total_chunks}"
        )

    except Exception as e:

        print("\n" + "=" * 60)
        print("Ingestion Failed")
        print("=" * 60)

        print(str(e))
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()