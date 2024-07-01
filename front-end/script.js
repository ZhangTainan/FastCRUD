const BaseURL = "http://localhost:8000/students/";

const $ = document.querySelector.bind(document);

const table = $("#table");
const tbody = $("#tbody");
const search_btn = $("#search-btn");
const keyword_input=$("#keyword");
let keyword = $("#keyword").value;
let page = 1, size = 5;





function getStudentList(keyword, page, size) {
    return axios.get(`${BaseURL}list`, {
        params: {
            keyword: keyword,
            page: page,
            size: size
        }
    })
}


function addRowToTable(student) {
    tbody.innerHTML += `
        <tr>
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.gender}</td>
            <td>${student.major}</td>
            <td class="options">
                <button @click="handleEdit(${student.id})">修改</button>
                <button @click="handleEdit(${student.id})">删除</button>
            </td>
        </tr>
    `
}

function addRowsToTable(students) {
    tbody.innerHTML=""
    students.forEach(student => {
        addRowToTable(student);
    });
}




getStudentList(keyword, page, size).then(res => {
    const { data: students } = res;
    addRowsToTable(students);
})


function search() {
    getStudentList(keyword,page,size).then(res => {
        tbody.innerHTML = ""
        const { data: list } = res;
        list.forEach(student => {
            addRowToTable(student);
        });
    })
}


keyword_input.addEventListener("input", (e) => {
    keyword=e.target.value;
});


search_btn.addEventListener("click", search);

