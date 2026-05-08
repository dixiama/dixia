// ===== MENU RESPONSIVE =====

const menuBtn = document.getElementById("menu-btn");

const nav = document.getElementById("nav");

menuBtn.addEventListener("click", () => {

    nav.classList.toggle("active");
});

// ===== DOCUMENTOS =====

const documentos = [

    // =========================
    // DISLEXIA
    // =========================

    {
        titulo: "DISLEXIA",

        descripcion: "Conceptos básicos sobre la dislexia.",

        imagenes: [

            "canvas/Dislexia/introDys.jpg",
            "canvas/Dislexia/introdyss.jpg",
            "canvas/Dislexia/Intreodis.jpg"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Ejercicios para practicar la lectura y escritura.",

        imagenes: [

            "canvas/Dislexia/act/1.png",
            "canvas/Dislexia/act/2.png",
            "canvas/Dislexia/act/3.png",
            "canvas/Dislexia/act/4.png",
            "canvas/Dislexia/act/5.png",
            "canvas/Dislexia/act/6.png"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Otras actividades para mejorar habilidades.",

        imagenes: [

            "canvas/Dislexia/act1/0.png",
            "canvas/Dislexia/act1/1.png",
            "canvas/Dislexia/act1/2.png",
            "canvas/Dislexia/act1/3.png",
            "canvas/Dislexia/act1/4.png"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Más ejercicios y prácticas.",

        imagenes: [

            "canvas/Dislexia/act2/1.png",
            "canvas/Dislexia/act2/2.png",
            "canvas/Dislexia/act2/3.png",
            "canvas/Dislexia/act2/4.png",
            "canvas/Dislexia/act2/5.png"
        ]
    },

    // =========================
    // DISGRAFIA
    // =========================

    {
        titulo: "DISGRAFÍA",

        descripcion: "Ejercicios para practicar la escritura y mejorar la motricidad fina.",

        imagenes: [

            "canvas/Disgrafia/act/0.png",
            "canvas/Disgrafia/act/1.png",
            "canvas/Disgrafia/act/2.png",
            "canvas/Disgrafia/act/3.png",
            "canvas/Disgrafia/act/4.png"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Ejercicios adicionales para mejorar la coordinación y precisión.",

        imagenes: [

            "canvas/Disgrafia/act1/1.png",
            "canvas/Disgrafia/act1/2.png",
            "canvas/Disgrafia/act1/3.png",
            "canvas/Disgrafia/act1/4.png",
            "canvas/Disgrafia/act1/5.png"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Más ejercicios prácticos para fortalecer habilidades.",

        imagenes: [

            "canvas/Disgrafia/act2/0.png",
            "canvas/Disgrafia/act2/1.png",
            "canvas/Disgrafia/act2/2.png",
            "canvas/Disgrafia/act2/3.png",
            "canvas/Disgrafia/act2/4.png"
        ]
    },

    // =========================
    // DISCALCULIA
    // =========================

    {
        titulo: "DISCALCULIA",

        descripcion: "Ejercicios matemáticos para mejorar habilidades numéricas.",

        imagenes: [

            "canvas/Discalculia/act 2/1.png",
            "canvas/Discalculia/act 2/2.png",
            "canvas/Discalculia/act 2/3.png",
            "canvas/Discalculia/act 2/4.png",
            "canvas/Discalculia/act 2/5.png",
            "canvas/Discalculia/act 2/6.png"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Ejercicios adicionales para mejorar habilidades matemáticas.",

        imagenes: [

            "canvas/Discalculia/act/0.png",
            "canvas/Discalculia/act/1.png",
            "canvas/Discalculia/act/2.png",
            "canvas/Discalculia/act/3.png",
            "canvas/Discalculia/act/4.png",
            "canvas/Discalculia/act/5.png"
        ]
    },

    {
        titulo: "ACTIVIDADES",

        descripcion: "Más ejercicios para fortalecer habilidades numéricas.",

        imagenes: [

            "canvas/Discalculia/act3/1.png",
            "canvas/Discalculia/act3/2.png",
            "canvas/Discalculia/act3/3.png",
            "canvas/Discalculia/act3/4.png",
            "canvas/Discalculia/act3/5.png"
        ]
    }
];

// ===== CONTENEDOR =====

const contenedor = document.getElementById("contenedor");

let intervalos = {};

// ===== CREAR CARDS =====

documentos.forEach((doc, index) => {

    const card = document.createElement("div");

    card.classList.add("card");

    card.innerHTML = `

        <img src="${doc.imagenes[0]}" alt="${doc.titulo}">

        <div class="card-content">

            <h2>${doc.titulo}</h2>

            <p>${doc.descripcion}</p>

        </div>

        <button class="download-btn">⬇</button>
    `;

    const img = card.querySelector("img");

    // ===== CARRUSEL =====

    let i = 0;

    card.addEventListener("mouseenter", () => {

        intervalos[index] = setInterval(() => {

            i = (i + 1) % doc.imagenes.length;

            img.src = doc.imagenes[i];

        }, 1500);
    });

    card.addEventListener("mouseleave", () => {

        clearInterval(intervalos[index]);

        img.src = doc.imagenes[0];
    });

    // ===== MODAL =====

    img.addEventListener("click", () => {

        const preview = document.getElementById("preview");

        preview.innerHTML = "";

        doc.imagenes.forEach(src => {

            const image = document.createElement("img");

            image.src = src;

            preview.appendChild(image);
        });

        document.getElementById("modal").style.display = "flex";
    });

    // ===== DESCARGAR ZIP =====

    card.querySelector(".download-btn").addEventListener("click", async (e) => {

        e.stopPropagation();

        const zip = new JSZip();

        const folder = zip.folder(doc.titulo.replace(/\s+/g, "_"));

        for(let i = 0; i < doc.imagenes.length; i++){

            const response = await fetch(doc.imagenes[i]);

            const blob = await response.blob();

            folder.file(`imagen_${i + 1}.jpg`, blob);
        }

        zip.generateAsync({type: "blob"}).then(content => {

            saveAs(content, `${doc.titulo.replace(/\s+/g, "_")}.zip`);
        });
    });

    contenedor.appendChild(card);
});

// ===== MODAL =====

const modal = document.getElementById("modal");

document.getElementById("closeModal").addEventListener("click", () => {

    modal.style.display = "none";
});

window.addEventListener("click", (e) => {

    if(e.target === modal){

        modal.style.display = "none";
    }
});