
//will be .oc I think

#include <gtk/gtk.h>
#include <vte/vte.h>
//sudo apt install libgtk-4-dev libvte-2.91-gtk4-dev
//cc `pkg-config --cflags vte-2.91-gtk4 gtk4` main.c `pkg-config --libs vte-2.91-gtk4 gtk4`

void q(gpointer terminal){
char *argv_test[3] = {
    "edor\0", NULL
};
vte_terminal_spawn_async(VTE_TERMINAL(terminal),VTE_PTY_DEFAULT,NULL,argv_test,NULL,G_SPAWN_DEFAULT,NULL,NULL,NULL,-1,NULL,NULL,NULL);
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *terminal;

  window = gtk_application_window_new (app);

    terminal = vte_terminal_new();

gtk_window_set_child((GtkWindow*)window,terminal);

gtk_widget_set_visible(window,TRUE);

g_idle_add_once(q,terminal);//g_timeout_add_once(2000,q,terminal);

}

int
main (int    argc,
      char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new (NULL, G_APPLICATION_DEFAULT_FLAGS);//G_APPLICATION_FLAGS_NONE
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
