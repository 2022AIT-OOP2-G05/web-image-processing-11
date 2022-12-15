const form = document.getElementById("form");
const fileInput = document.getElementById("file-input");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  postImg();
});

const postImg = async () => {
  const formData = new FormData(form);
  const fileInput = document.getElementById("file-input");

  formData.append("file", fileInput.files[0]);

  try {
    await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    fileInput.value = "";
  } catch (err) {
    console.log(err);
  }
};
