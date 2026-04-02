<template>
  <div class="editor-container">
    <editor-content :editor="editor" class="tiptap-viewport" />
  </div>
</template>

<script setup>
import { onBeforeUnmount } from "vue";
import { useEditor, EditorContent } from "@tiptap/vue-3";
import StarterKit from "@tiptap/starter-kit";
import { Node, mergeAttributes } from "@tiptap/core";

// 1. Definimos la extensión personalizada "Page"
const Page = Node.create({
  name: "page",
  group: "block",
  content: "block+", // Permite párrafos, listas, etc. dentro de la página
  defining: true, // Ayuda a mantener la estructura al pegar texto

  addAttributes() {
    return {
      number: {
        default: null,
        parseHTML: (element) => element.getAttribute("data-number"),
        renderHTML: (attributes) => ({ "data-number": attributes.number }),
      },
      id: {
        default: null,
        parseHTML: (element) => element.getAttribute("id"),
        renderHTML: (attributes) => ({ id: attributes.id }),
      },
    };
  },

  parseHTML() {
    return [{ tag: 'div[data-type="page"]' }];
  },

  renderHTML({ HTMLAttributes }) {
    // Añadimos la clase 'page-virtual' para el CSS de rendimiento
    return [
      "div",
      mergeAttributes(HTMLAttributes, {
        "data-type": "page",
        class: "page-virtual",
      }),
      0,
    ];
  },
});

// 2. Props para recibir el HTML ya "empaquetado" desde Python
const props = defineProps({
  initialContent: {
    type: String,
    default: "",
  },
});

// 3. Inicialización del Editor
const editor = useEditor({
  content: props.initialContent,
  extensions: [
    StarterKit,
    Page, // Nuestra extensión de páginas
  ],
  editorProps: {
    attributes: {
      spellcheck: "false",
      class: "prose-container", // Clase para estilos generales de texto
    },
  },
});

onBeforeUnmount(() => {
  editor.value.destroy();
});
</script>

<style>
:root {
  --c-bg:       #141414;  /* fondo base */
  --c-surface:  #1c1c1c;  /* sidebars, topbar */
  --c-raised:   #242424;  /* elementos elevados, hover */
  
  --c-border:   #2e2e2e;  /* bordes sutiles */
  --c-border2:  #3a3a3a;  /* bordes con énfasis */
  --c-faint:    #3d3d3d;  /* fills inactivos */
  --c-muted:    #6a6a6a;  /* texto terciario, labels */
  --c-text2:    #9a9590;  /* texto secundario */
  --c-text:     #e0dbd2;  /* texto principal */
  --c-accent2:  #c4b89a;  /* acento secundario, bordes activos */
  --c-accent:   #e8e0d0;  /* acento principal, títulos */

  /* semánticas */
  --c-red:      #c0432b;
  --c-amber:    #b07830;
  --c-green:    #4a7c54;

  /* layout */
  --r:          3px;      /* border-radius base */
}


/* --- CAPA DE RENDIMIENTO (CRÍTICO) --- */
.editor-container {
  /* Establece cuánto espacio quieres que ocupe el editor en pantalla */
  height: 100vh; /* Ocupa todo el alto de la ventana */
  overflow-y: auto; /* Activa el scroll vertical cuando el contenido sea mayor a 100vh */
  background: var(--c-bg);
}

.tiptap-viewport {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 20px;
}

.tiptap-viewport .ProseMirror {
  min-height: 100%;
  outline: none;
}

.page-virtual {
  /* La magia: el navegador no dibuja la página si no está en el viewport */
  content-visibility: auto;

  /* Evita que el scrollbar "tiemble". Ajusta 1100px a la altura real de tu página */
  contain-intrinsic-size: 1px 1100px;

  background: var(--c-surface);
  margin-bottom: 40px;
  padding: 60px 80px;
  position: relative;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border-radius: 4px;

  display: block;
  content-visibility: auto;
  contain-intrinsic-size: 1px 1100px; /* Muy importante para el scrollbar */
  min-height: 100px;
}

/* --- INDICADOR DE PÁGINA (ESTÉTICO) --- */

.page-virtual::before {
  /* Toma el número del atributo data-number automáticamente */
  content: "PÁGINA " attr(data-number);
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 11px;
  font-weight: bold;
  color: #c0c0c0;
  letter-spacing: 1px;
  user-select: none; /* Evita que el número se seleccione al copiar texto */
  pointer-events: none; /* El ratón lo atraviesa para no estorbar la edición */
}

/* Estilos de texto básicos para que se vea bien */
.prose-container:focus {
  outline: none;
}

.page-virtual p {
  line-height: 1.6;
  margin-bottom: 1rem;
}

.page-virtual ul {
  padding-left: 1.5rem;
  margin-bottom: 1rem;
}
</style>
