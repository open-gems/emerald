import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useDocumentStore = defineStore("document", () => {
  const fakeFolders = [
    {
      id: "019d265f-79d6-7f8f-a0e8-73d727d70cd0",
      user_id: "019d2612-a01d-734c-ab63-917106f31187",
      status: "created",
      name: "folder1",
      storage_path:
        "/storage/019d2612-a01d-734c-ab63-917106f31187/019d265f-79d6-7f8f-a0e8-73d727d70cd0",
      document_count: 2,
      color: "red",
      created_at: 1774465284566,
      readed_at: null,
      updated_at: null,
      deleted_at: null,
      v: 0,
    },
    {
      id: "019d2635-52d8-7e32-8147-660bf092e2e9",
      user_id: "019d2612-a01d-734c-ab63-917106f31187",
      status: "created",
      name: "folder2",
      storage_path:
        "/storage/019d2612-a01d-734c-ab63-917106f31187/019d2635-52d8-7e32-8147-660bf092e2e9",
      document_count: 6,
      color: "red",
      created_at: 1774462522072,
      readed_at: null,
      updated_at: null,
      deleted_at: null,
      v: 0,
    },
  ];

  const folders = ref(fakeFolders);

  const filteredFolders = computed(() =>
    folders.value.filter((folder) => folder.status === "created"),
  );

  return { folders, filteredFolders };
});
