 const documentos = [
      {
        titulo: "ACTIVIDADES",
        descripcion: "Ejercicios matemáticos para mejorar habilidades numéricas.",
        imagenes: [
          "canvas/Discalculia/act 2/1.png",
          "canvas/Discalculia/act 2/2.png",
          "canvas/Discalculia/act 2/3.png",
          "canvas/Discalculia/act 2/4.png",
          "canvas/Discalculia/act 2/5.png",
          "canvas/Discalculia/act 2/6.png",
        ],
      
      },
            {
        titulo: "ACTIVIDADES 2",
        descripcion: "Ejercicios adicionales para mejorar habilidades matemáticas.",
        imagenes: [
          "canvas/Discalculia/act/0.png",
          "canvas/Discalculia/act/1.png",
          "canvas/Discalculia/act/2.png",
          "canvas/Discalculia/act/3.png",
          "canvas/Discalculia/act/4.png",
          "canvas/Discalculia/act/5.png",
        ],
      
      },      {
        titulo: "ACTIVIDADES 3",
        descripcion: "Más ejercicios para fortalecer habilidades numéricas.",
        imagenes: [
          "canvas/Discalculia/act3/1.png",
          "canvas/Discalculia/act3/2.png",
          "canvas/Discalculia/act3/3.png",
          "canvas/Discalculia/act3/4.png",
          "canvas/Discalculia/act3/5.png",
        ],
      
      },    
    ];

    const contenedor = document.getElementById("contenedor");
    let intervalos = {}; // para manejar carruseles

    documentos.forEach((doc, index) => {
      const card = document.createElement("div");
      card.classList.add("card");

      card.innerHTML = `
        <img src="${doc.imagenes[0]}" alt="${doc.titulo}" data-index="0">
        <div class="card-content">
          <h2>${doc.titulo}</h2>
          <p>${doc.descripcion}</p>
        </div>
        <span class="badge">${doc.badge}</span>
        <button class="download-btn">⬇</button>
      `;

      // Carrusel automático al hover
      const img = card.querySelector("img");
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

      // Abrir modal (preview)
      card.querySelector("img").addEventListener("click", () => {
        const previewDiv = document.getElementById("preview");
        previewDiv.innerHTML = "";
        doc.imagenes.forEach(src => {
          const imageEl = document.createElement("img");
          imageEl.src = src;
          previewDiv.appendChild(imageEl);
        });
        document.getElementById("modal").style.display = "flex";
      });

      // Descargar todas las imágenes en ZIP
      card.querySelector(".download-btn").addEventListener("click", async () => {
        const zip = new JSZip();
        const folder = zip.folder(doc.titulo.replace(/\s+/g, "_"));

        // Descargar cada imagen como blob
        for (let idx = 0; idx < doc.imagenes.length; idx++) {
          const url = doc.imagenes[idx];
          const response = await fetch(url);
          const blob = await response.blob();
          folder.file(`pagina_${idx + 1}.jpg`, blob);
        }

        // Generar y guardar ZIP
        zip.generateAsync({ type: "blob" }).then(content => {
          saveAs(content, `${doc.titulo.replace(/\s+/g, "_")}.zip`);
        });
      });

      contenedor.appendChild(card);
    });

    // Modal cerrar
    const modal = document.getElementById("modal");
    document.getElementById("closeModal").onclick = () => modal.style.display = "none";