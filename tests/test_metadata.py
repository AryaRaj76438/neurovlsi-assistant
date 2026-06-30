from src.metadata.metadata_generator import MetadataGenerator

generator = MetadataGenerator()

text = """
A current mirror is widely used in analog CMOS
circuits. The MOSFET devices operate in saturation.
"""

metadata = generator.generate(text)

print(metadata)