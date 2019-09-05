import axios from "axios";

export function getNote() {
  // return axios.get("https://jsonplaceholder.typicode.com/posts/" + postId);
  return axios.get("http://127.0.0.1:8000/api/v1/memos/");
}
export function postNote(obj) {
  // console.log(obj);
  return axios.post("http://127.0.0.1:8000/api/v1/memos/",{
    ...obj
  });
}
//
// export function getComments(postId) {
//   return axios.get(
//     `https://jsonplaceholder.typicode.com/posts/${postId}/comments`
//   );
// }
