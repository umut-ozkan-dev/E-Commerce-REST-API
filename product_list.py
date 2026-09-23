from typing import Dict

# Small Images
im1 = "https://i.ibb.co/7dLCRxDv/image-9.webp"
im2 = "https://i.ibb.co/jvnd2Ptv/image-2.webp"
im3 = "https://cdn.myimgs.org/images/43305/image_3.png"
im4 = "https://i.ibb.co/bgmXn67N/image-4.webp"
im5 = "https://i.ibb.co/VpwddzLv/image-5.webp"
im6 = "https://i.ibb.co/Fb1HVG7j/image-6.webp"
im7 = "https://i.ibb.co/994w97Kq/image-8.webp"
im8 = "https://i.ibb.co/9mN3PSnp/image-1.webp"
im9 = "https://i.ibb.co/mFzMDR4G/image-10.webp"
im10 = "https://i.ibb.co/Q7HWtZX2/image-11.webp"
im11 = "https://ibb.co/XZ3tt4TC"
im12 = "https://i.ibb.co/jZhchyMY/image-12.webp"
im13 = "https://i.ibb.co/YBd53w8w/image-13.webp"
im14 = "https://i.ibb.co/sdbqgcKh/image-14.webp"
im15 = "https://i.ibb.co/gMj7KTCp/image-15.webp"
im16 = "https://i.ibb.co/7tWQZffc/image-16.webp"
im17 = "https://i.ibb.co/pr1VMqx6/image-17.webp"
im18 = "https://i.ibb.co/Kzp16dSD/image-18.webp"
im19 = "https://i.ibb.co/Fb8GqyGX/image-19.webp"
im20 = "https://i.ibb.co/jZsB6Vgm/image-20.webp"
im21 = "https://i.ibb.co/N2MgdM64/image-21.png"
im22 = "https://i.ibb.co/PzGqL2m5/image-22.webp"
im23 = "https://i.ibb.co/Tx8hTPQ9/image-23.webp"
im24 = "https://i.ibb.co/fzWkQjL5/image-24.webp"
im25 = "https://i.ibb.co/Rrvwk7V/image-25.webp"
im26 = "https://i.ibb.co/zh9MWSCy/image-26.webp"
im27 = "https://i.ibb.co/7NYX113g/image-27.webp"
im28 = "https://i.ibb.co/BXW4kBv/image-28.webp"
im29 = "https://i.ibb.co/GQ6TNc2f/image-29.webp"
im30 = "https://i.ibb.co/JRbDNMYP/image-30.webp"
im31 = "https://i.ibb.co/Fq3v7tp2/image-31.webp"
im32 = "https://i.ibb.co/Lzw3s5Tm/image-32.webp"
im33 = "https://i.ibb.co/3JJr4Vw/image-33.webp"
im34 = "https://i.ibb.co/PZ4Z8p3j/image-34.webp"
im35 = "https://i.ibb.co/DgfmWVSC/image-35.webp"
im36 = "https://i.ibb.co/rRjz0SxK/image-36.webp"
im37 = "https://i.ibb.co/qYLJmcRg/image-37.webp"
im38 = "https://i.ibb.co/pv18srFp/image-38.webp"
im39 = "https://i.ibb.co/pv3JsHKB/image-39.webp"
im40 = " https://i.ibb.co/Tqq9s4Bk/image-40.webp"
im41 = "https://i.ibb.co/bM0K0qRG/image-41.webp"
im42 = "https://i.ibb.co/RpXYD8zm/image-42.webp"

# Large Images
IMG1 = "https://i.ibb.co/n8Z1xw8B/image-8.png"
IMG2 = "https://i.ibb.co/Z6ZGkVHH/image-2.png"
IMG3 = "https://i.ibb.co/4RVPgDfk/image-3.png"
IMG4 = "https://i.ibb.co/4RBNgzBj/image-4.png"
IMG5 = "https://i.ibb.co/JWhDmdqG/image-5.png"
IMG6 = "https://i.ibb.co/dsNtgwBS/image-6.png"
IMG7 = "https://i.ibb.co/bMXTjjqk/image-7-1.png"
IMG8 = "https://i.ibb.co/gZWjpj4X/image-1.png"
IMG9 = "https://i.ibb.co/HDRkdrXt/image-9.png"


product_list: list[Dict] = [
    {
        "id": 1,
        "Name": "TerraStore Large Green Tent",
        "Price": 299.99,
        "Quantity ": 22,
        "Category": "Tent",
        "Img": im1,
    },
    {
        "id": 2,
        "Name": "PineCoal Fire-Starting Kit",
        "Price": 49.99,
        "In Stock": True,
        "Img": im2,
    },
    {
        "id": 3,
        "Name": "TerraStore Large Headlight Orange ",
        "Price": 29.99,
        "In Stock": True,
        "Img": im3,
    },
    {
        "id": 4,
        "Name": "Frosty Small Sleeping Mat ",
        "Price": 199.99,
        "In Stock": True,
        "Img": im4,
    },
    {
        "id": 5,
        "Name": "Mountain 20L Blue Backpack",
        "Price": 179.99,
        "In Stock": True,
        "Img": im5,
    },
    {
        "id": 6,
        "Name": "TerraStore 15L Container",
        "Price": 49.99,
        "In Stock": True,
        "Img": im6,
    },
    {
        "id": 7,
        "Name": "IronTrail Camping Utensils Set",
        "Price": 39.99,
        "In Stock": True,
        "Img": im7,
    },
    {
        "id": 8,
        "Name": "TerraStore Medium Orange Tent",
        "Price": 279.99,
        "In Stock": True,
        "Img": im8,
    },
    {
        "id": 9,
        "Name": "PineCoal Single Portable Stove",
        "Price": 59.99,
        "In Stock": True,
        "Img": im9,
    },
    {
        "id": 10,
        "Name": "Frosty 1.5L Stainless Steel Thermos",
        "Price": 79.99,
        "In Stock": True,
        "Img": im10,
    },
    {"id": 11, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im12},
    {"id": 12, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im23},
    {"id": 13, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im13},
    {"id": 14, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im14},
    {"id": 15, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im15},
    {"id": 16, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im16},
    {"id": 17, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im17},
    {"id": 18, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im18},
    {"id": 19, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im19},
    {"id": 20, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im20},
    {"id": 21, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im21},
    {"id": 22, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im22},
    {"id": 23, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im23},
    {"id": 24, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im24},
    {"id": 25, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im25},
    {"id": 26, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im26},
    {"id": 27, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im27},
    {"id": 28, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im28},
    {"id": 29, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im29},
    {"id": 30, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im30},
    {"id": 31, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im31},
    {"id": 32, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im32},
    {"id": 33, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im33},
    {"id": 34, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im34},
    {"id": 35, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im35},
    {"id": 36, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im36},
    {"id": 37, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im37},
    {"id": 38, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im38},
    {"id": 39, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im39},
    {"id": 40, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im40},
    {"id": 41, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im41},
    {"id": 42, "Name": " Monitor", "Price": 79.99, "In Stock": True, "Img": im42},
]
