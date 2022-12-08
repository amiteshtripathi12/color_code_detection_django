
const imageUploadInput = document.getElementById("imageUpload");
let imageUploadPreviewContainer = document.getElementById("imageUploadPreviewContainer")


imageUploadInput.addEventListener("input",(event)=>{
    let uploadFile = event.target.files[0];
    if (uploadFile){

        const img = document.createElement("img");
        img.classList.add("obj");
        img.file = uploadFile;
        // preview.appendChild(img); // Assuming that "preview" is the div output where the content will be displayed.

        const reader = new FileReader();
        reader.onload = (e) => { img.src = e.target.result; };
        reader.readAsDataURL(uploadFile);

        img.style.width = "100%";
        img.style.borderRadius = "20px";
        img.style.filter = "drop-shadow(2px 2px 4px rgba(9, 6, 4, 0.553))";
        imageUploadPreviewContainer.append(img)
    }
});