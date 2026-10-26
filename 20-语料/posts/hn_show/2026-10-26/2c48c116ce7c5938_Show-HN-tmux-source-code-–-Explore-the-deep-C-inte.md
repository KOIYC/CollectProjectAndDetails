---
type: "corpus"
item_id: "2c48c116ce7c5938"
title: "Show HN: tmux source code – Explore the deep C internals"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50234737"
project_url: "https://libtmux.org/en/tmux/latest/reference"
author: "tony"
published_at: "2026-10-25T18:45:02Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-26"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_tony
  - story_50234737
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: tmux source code – Explore the deep C internals

> [!info] 一句话导读
> libtmux tmux CLI tmux tmux CLI Python Ruby Lua PowerShell Julia Elixir TypeScript Rust Go Java Kotlin Scala C# F# C++ Swift Choose a port 16

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50234737>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：tony　|　发布：2026-10-25T18:45:02Z
> 项目链接：<https://libtmux.org/en/tmux/latest/reference>
> 采集：2026-10-26T09:42:36+08:00　|　id：`2c48c116ce7c5938`

## 正文

libtmux tmux CLI tmux tmux CLI Python Ruby Lua PowerShell Julia Elixir TypeScript Rust Go Java Kotlin Scala C# F# C++ Swift Choose a port 16
 Find a port Scripting & web
 Python Ruby Lua Julia TypeScript
 Compiled & native
 Rust Go C++ Swift
 JVM
 Java Kotlin Scala
 .NET
 C# F# PowerShell
 BEAM
 Elixir
 tmux
 tmux CLI ✓ → No matching ports.
Search Colour scheme Auto Light Dark
 Menu Reference
tmux tmux C source reference Choose documentation 1
 Find an app or section tmux Commands, configuration and terminal workflows Home Guides Concepts Examples Topics CLI Manual Options, hooks and formats Catalog C source reference C reference ✓
No matching documentation.
tmux · latest · en
Back latest tmux source version
 Find a version No matching versions.
Latest (3.7c) ✓ 3.7c 3.2a
 English Available translations No matching languages.
English ✓
 Translation coverage
tmux C API contents
tmux C API
Find a type or member /
 All Types Members
Choose type
 No types found.
All types Reveal current Collapse all Outline Focus Grouped
 Up Root
Retry search Server 52
Session 64
Window 443
Pane 87
Client 143
Commands 463
Options and formats 502
Screen and terminal 770
Layouts and buffers 106
Supporting declarations 1076
tmux
 / Reference (3.7c)
 Copy Markdown Print
tmux C source reference
 C declarations from tmux 3.7c. These are tmux internals, not a supported external library API.
 Paths through the source #
 Follow these functions to explore a task. Arrows show source relationships.
 Create a session and its first pane
 cmd_new_session_exec
 calls → spawn_window
 calls → spawn_pane
 calls → window_add_pane
 calls → window_pane_create
Split a window
 cmd_split_window_exec
 references → spawn_pane
 calls → window_add_pane
 calls → window_pane_create
Start the server and create a client
 server_start
 calls → server_client_create
 calls → proc_add_peer
Server 7 functions and constants f server_start function
f server_create_socket function
f server_update_socket function
f server_check_unattached function
f server_destroy_session function
f server_kill_window function
f server_kill_pane function
Server — Supporting declarations 45 functions and constants a current_time attribute
a marked_pane attribute
a message_log attribute
a message_next attribute
a server_ev_accept attribute
a server_ev_tidy attribute
a server_exit attribute
a server_fd attribute
a server_proc attribute
f server_accept function
f server_add_accept function
f server_add_message function
f server_check_marked function
f server_child_exited function
f server_child_signal function
f server_child_stopped function
f server_clear_marked function
f server_destroy_pane function
f server_destroy_session_group function
f server_find_session function
f server_is_marked function
f server_link_window function
f server_lock function
f server_lock_client function
f server_lock_session function
f server_loop function
f server_newer_detached_session function
f server_newer_session function
f server_redraw_client function
f server_redraw_session function
f server_redraw_session_group function
f server_redraw_window function
f server_redraw_window_borders function
f server_renumber_all function
f server_renumber_session function
f server_send_exit function
f server_set_marked function
f server_signal function
f server_status_client function
f server_status_session function
f server_status_session_group function
f server_status_window function
f server_tidy_event function
f server_unlink_window function
f server_unzoom_window function
Session 1 type, 8 functions and constants S session struct 23 members
f session_create function
f session_find function
f session_find_by_id function
f session_attach function
f session_detach function
f session_select function
f session_set_current function
f session_destroy function
Session — Supporting declarations 3 types, 52 functions and constants S session_group struct 5 members
S session_groups struct 1 member
S sessions struct 1 member
a next_session_id attribute
a session_groups attribute
a sessions attribute
f session_add_ref function
f session_alive function
f session_cmp function
f session_find_by_id_str function
f session_free function
f session_group_add function
f session_group_attached_count function
f session_group_cmp function
f session_group_contains function
f session_group_count function
f session_group_find function
f session_group_new function
f session_group_remove function
f session_group_synchronize_from function
f session_group_synchronize_to function
f session_group_synchronize1 function
f session_groups_RB_FIND function
f session_groups_RB_INSERT function
f session_groups_RB_INSERT_COLOR function
f session_groups_RB_MINMAX function
f session_groups_RB_NEXT function
f session_groups_RB_NFIND function
f session_groups_RB_PREV function
f session_groups_RB_REMOVE function
f session_groups_RB_REMOVE_COLOR function
f session_has function
f session_is_linked function
f session_last function
f session_lock_timer function
f session_next function
f session_next_alert function
f session_next_session function
f session_previous function
f session_previous_alert function
f session_previous_session function
f session_remove_ref function
f session_renumber_windows function
f session_theme_changed function
f session_update_activity function
f session_update_history function
f sessions_RB_FIND function
f sessions_RB_INSERT function
f sessions_RB_INSERT_COLOR function
f sessions_RB_MINMAX function
f sessions_RB_NEXT function
f sessions_RB_NFIND function
f sessions_RB_PREV function
f sessions_RB_REMOVE function
f sessions_RB_REMOVE_COLOR function
Window 2 types, 6 functions and constants S window struct 42 members
S winlink struct 10 members
f window_create function
f window_find_by_id function
f window_set_active_pane function
f window_add_pane function
f window_remove_pane function
f window_resize function
Window — Supporting declarations 22 types, 413 functions and constants S window_copy_cmd_table (anonymous struct) struct 7 members
S window_buffer_editdata struct 3 members
S window_buffer_itemdata struct 3 members
S window_buffer_modedata struct 8 members
S window_client_itemdata struct 1 member
S window_client_modedata struct 7 members
S window_clock_mode_data struct 3 members
S window_copy_cmd_state struct 7 members
S window_copy_mode_data struct 54 members
S window_customize_itemdata struct 7 members
S window_customize_modedata struct 11 members
S window_tree_itemdata struct 4 members
S window_tree_modedata struct 20 members
S windows struct 1 member
S winlink_stack struct 2 members
S winlinks struct 1 member
E window_copy_cmd_action enum 3 members
E window_copy_cmd_clear enum 3 members
E window_copy_line_numbers enum 5 members
E window_customize_scope enum 8 members
E window_customize_change enum 2 members
E window_tree_type enum 4 members
a all_window_panes attribute
a next_active_point attribute
a next_window_id attribute
a next_window_pane_id attribute
a window_buffer_help_lines attribute
a window_buffer_menu_items attribute
a window_buffer_mode attribute
a window_buffer_order_seq attribute
a window_client_help_lines attribute
a window_client_menu_items attribute
a window_client_mode attribute
a window_client_order_seq attribute
a window_clock_mode attribute
a window_clock_table attribute
a window_copy_cmd_table attribute
a window_copy_mode attribute
a window_customize_help_lines attribute
a window_customize_menu_items attribute
a window_customize_mode attribute
a window_tree_help_lines attribute
a window_tree_menu_items attribute
a window_tree_mode attribute
a window_tree_order_seq attribute
a window_view_mode attribute
a windows attribute
f window_add_ref function
f window_buffer_add_item function
f window_buffer_build function
f window_buffer_do_delete function
f window_buffer_do_paste function
f window_buffer_draw function
f window_buffer_edit_close_cb function
f window_buffer_find function
f window_buffer_finish_edit function
f window_buffer_free function
f window_buffer_free_item function
f window_buffer_get_key function
f window_buffer_help function
f window_buffer_init function
f window_buffer_key function
f window_buffer_menu function
f window_buffer_resize function
f window_buffer_search function
f window_buffer_sort function
f window_buffer_start_edit function
f window_buffer_update function
f window_client_add_item function
f window_client_build function
f window_client_do_detach function
f window_client_draw function
f window_client_free function
f window_client_free_item function
f window_client_get_key function
f window_client_help function
f window_client_init function
f window_client_key function
f window_client_menu function
f window_client_resize function
f window_client_sort function
f window_client_update function
f window_clock_draw_screen function
f window_clock_free function
f window_clock_init function
f window_clock_key function
f window_clock_resize function
f window_clock_start_timer function
f window_clock_timer_callback function
f window_cmp function
f window_copy_acquire_cursor_down function
f window_copy_acquire_cursor_up function
f window_copy_add function
f window_copy_adjust_selection function
f window_copy_append_selection function
f window_copy_cellstring function
f window_copy_clear_marks function
f window_copy_clear_selection function
f window_copy_clip_width function
f window_copy_clone_screen function
f window_copy_cmd_append_selection function
f window_copy_cmd_append_selection_and_cancel function
f window_copy_cmd_back_to_indentation function
f window_copy_cmd_begin_selection function
f window_copy_cmd_bottom_line function
f window_copy_cmd_cancel function
f window_copy_cmd_centre_horizontal function
f window_copy_cmd_centre_vertical function
f window_copy_cmd_clear_selection function
f window_copy_cmd_copy_end_of_line function
f window_copy_cmd_copy_end_of_line_and_cancel function
f window_copy_cmd_copy_line function
f window_copy_cmd_copy_line_and_cancel function
f window_copy_cmd_copy_pipe function
f window_copy_cmd_copy_pipe_and_cancel function
f window_copy_cmd_copy_pipe_end_of_line function
f window_copy_cmd_copy_pipe_end_of_line_and_cancel function
f window_copy_cmd_copy_pipe_line function
f window_copy_cmd_copy_pipe_line_and_cancel function
f window_copy_cmd_copy_pipe_no_clear function
f window_copy_cmd_copy_selection function
f window_copy_cmd_copy_selection_and_cancel function
f window_copy_cmd_copy_selection_no_clear function
f window_copy_cmd_cursor_down function
f window_copy_cmd_cursor_down_and_cancel function
f window_copy_cmd_cursor_left function
f window_copy_cmd_cursor_right function
f window_copy_cmd_cursor_up function
f window_copy_cmd_end_of_line function
f window_copy_cmd_goto_line function
f window_copy_cmd_halfpage_down function
f window_copy_cmd_halfpage_down_and_cancel function
f window_copy_cmd_halfpage_up function
f window_copy_cmd_history_bottom function
f window_copy_cmd_history_top function
f window_copy_cmd_jump_again function
f window_copy_cmd_jump_backward function
f window_copy_cmd_jump_forward function
f window_copy_cmd_jump_reverse function
f window_copy_cmd_jump_to_backward function
f window_copy_cmd_jump_to_forward function
f window_copy_cmd_jump_to_mark function
f window_copy_cmd_middle_line function
f window_copy_cmd_next_matching_bracket function
f window_copy_cmd_next_paragraph function
f window_copy_cmd_next_prompt function
f window_copy_cmd_next_space function
f window_copy_cmd_next_space_end function
f window_copy_cmd_next_word function
f window_copy_cmd_next_word_end function
f window_copy_cmd_other_end function
f window_copy_cmd_page_down function
f window_copy_cmd_page_down_and_cancel function
f window_copy_cmd_page_up function
f window_copy_cmd_pipe function
f window_copy_cmd_pipe_and_cancel function
f window_copy_cmd_pipe_no_clear function
f window_copy_cmd_previous_matching_bracket function
f window_copy_cmd_previous_paragraph function
f window_copy_cmd_previous_prompt function
f window_copy_cmd_previous_space function
f window_copy_cmd_previous_word function
f window_copy_cmd_recentre_top_bottom function
f window_copy_cmd_rectangle_off function
f window_copy_cmd_rectangle_on function
f window_copy_cmd_rectangle_toggle function
f window_copy_cmd_refresh_from_pane function
f window_copy_cmd_scroll_bottom function
f window_copy_cmd_scroll_down function
f window_copy_cmd_scroll_down_and_cancel function
f window_copy_cmd_scroll_exit_off function
f window_copy_cmd_scroll_exit_on function
f window_copy_cmd_scroll_exit_toggle function
f window_copy_cmd_scroll_middle function
f window_copy_cmd_scroll_to function
f window_copy_cmd_scroll_to_mouse function
f window_copy_cmd_scroll_top function
f window_copy_cmd_scroll_up function
f window_copy_cmd_search_again function
f window_copy_cmd_search_backward function
f window_copy_cmd_search_backward_incremental function
f window_copy_cmd_search_backward_text function
f window_copy_cmd_search_forward function
f window_copy_cmd_search_forward_incremental function
f window_copy_cmd_search_forward_text function
f window_copy_cmd_search_reverse function
f window_copy_cmd_select_line function
f window_copy_cmd_select_word function
f window_copy_cmd_selection_mode function
f window_copy_cmd_set_mark function
f window_copy_cmd_start_of_line function
f window_copy_cmd_stop_selection function
f window_copy_cmd_toggle_position function
f window_copy_cmd_top_line function
f window_copy_command function
f window_copy_common_init function
f window_copy_copy_buffer function
f window_copy_copy_line function
f window_copy_copy_pipe function
f window_copy_copy_selection function
f window_copy_cstrtocellpos function
f window_copy_cursor_back_to_indentation function
f window_copy_cursor_down function
f window_copy_cursor_end_of_line function
f window_copy_cursor_hyperlink_cb function
f window_copy_cursor_jump function
f window_copy_cursor_jump_back function
f window_copy_cursor_jump_to function
f window_copy_cursor_jump_to_back function
f window_copy_cursor_left function
f window_copy_cursor_limit function
f window_copy_cursor_line_cb function
f window_copy_cursor_next_word function
f window_copy_cursor_next_word_end function
f window_copy_cursor_next_word_end_pos function
f window_copy_cursor_offset function
f window_copy_cursor_previous_word function
f window_copy_cursor_previous_word_pos function
f window_copy_cursor_prompt function
f window_copy_cursor_right function
f window_copy_cursor_start_of_line function
f window_copy_cursor_unoffset function
f window_copy_cursor_up function
f window_copy_cursor_word_cb function
f window_copy_do_copy_end_of_line function
f window_copy_do_copy_line function
f window_copy_drag_release function
f window_copy_drag_update function
f window_copy_expand_search_string function
f window_copy_find_length function
f window_copy_formats function
f window_copy_free function
f window_copy_get_current_offset function
f window_copy_get_hyperlink function
f window_copy_get_line function
f window_copy_get_screen function
f window_copy_get_selection function
f window_copy_get_word function
f window_copy_goto_line function
f window_copy_in_set function
f window_copy_init function
f window_copy_init_ctx_cb function
f window_copy_is_lowercase function
f window_copy_jump_to_mark function
f window_copy_key_table function
f window_copy_last_regex function
f window_copy_line_number_is_absolute function
f window_copy_line_number_mode function
f window_copy_line_number_width function
f window_copy_line_numbers_active function
f window_copy_match_at_cursor function
f window_copy_match_start_end function
f window_copy_move_after_search_mark function
f window_copy_move_left function
f window_copy_move_mouse function
f window_copy_move_right function
f window_copy_next_paragraph function
f window_copy_other_end function
f window_copy_pagedown function
f window_copy_pagedown1 function
f window_copy_pageup function
f window_copy_pageup1 function
f window_copy_pipe function
f window_copy_pipe_run function
f window_copy_previous_paragraph function
f window_copy_rectangle_set function
f window_copy_redraw_lines function
f window_copy_redraw_screen function
f window_copy_redraw_selection function
f window_copy_resize function
f window_copy_scroll function
f window_copy_scroll_down function
f window_copy_scroll_timer function
f window_copy_scroll_to function
f window_copy_scroll_up function
f window_copy_scroll1 function
f window_copy_search function
f window_copy_search_back_overlap function
f window_copy_search_compare function
f window_copy_search_down function
f window_copy_search_jump function
f window_copy_search_lr function
f window_copy_search_lr_regex function
f window_copy_search_mark_at function
f window_copy_search_mark_match function
f window_copy_search_marks function
f window_copy_search_match_cb function
f window_copy_search_rl function
f window_copy_search_rl_regex function
f window_copy_search_up function
f window_copy_set_line_numbers function
f window_copy_set_selection function
f window_copy_size_changed function
f window_copy_start_drag function
f window_copy_start_selection function
f window_copy_stringify function
f window_copy_style_changed function
f window_copy_synchronize_cursor function
f window_copy_synchronize_cursor_end function
f window_copy_update_cursor function
f window_copy_update_selection function
f window_copy_update_style function
f window_copy_vadd function
f window_copy_view_init function
f window_copy_visible_lines function
f window_copy_write_line function
f window_copy_write_lines function
f window_copy_write_one function
f window_count_panes function
f window_customize_add_item function
f window_customize_build function
f window_customize_build_array function
f window_customize_build_keys function
f window_customize_build_option function
f window_customize_build_options function
f window_customize_change_current_callback function
f window_customize_change_each function
f window_customize_change_tagged_callback function
f window_customize_check_item function
f window_customize_destroy function
f window_customize_draw function
f window_customize_draw_key function
f window_customize_draw_option function
f window_customize_find_user_options function
f window_customize_free function
f window_customize_free_callback function
f window_customize_free_item function
f window_customize_free_item_callback function
f window_customize_get_key function
f window_customize_get_tag function
f window_customize_get_tree function
f window_customize_height function
f window_customize_help function
f window_customize_init function
f window_customize_key function
f window_customize_menu function
f window_customize_reset_key function
f window_customize_reset_option function
f window_customize_resize function
f window_customize_scope_text function
f window_customize_set_command_callback function
f window_customize_set_key function
f window_customize_set_note_callback function
f window_customize_set_option function
f window_customize_set_option_callback function
f window_customize_unset_key function
f window_customize_unset_option function
f window_destroy function
f window_destroy_panes function
f window_find_by_id_str function
f window_find_string function
f window_get_active_at function
f window_get_bg_client function
f window_has_floating_panes function
f window_has_pane function
f window_lost_pane function
f window_pop_zoom function
f window_printable_flags function
f window_push_zoom function
f window_redraw_active_switch function
f window_remove_ref function
f window_set_fill_character function
f window_set_name function
f window_tree_add_item function
f window_tree_build function
f window_tree_build_pane function
f window_tree_build_session function
f window_tree_build_window function
f window_tree_command_callback function
f window_tree_command_done function
f window_tree_command_each function
f window_tree_command_free function
f window_tree_destroy function
f window_tree_draw function
f window_tree_draw_label function
f window_tree_draw_session function
f window_tree_draw_window function
f window_tree_filter_pane function
f window_tree_free function
f window_tree_free_item function
f window_tree_get_key function
f window_tree_get_target function
f window_tree_help function
f window_tree_init function
f window_tree_key function
f window_tree_kill_current_callback function
f window_tree_kill_each function
f window_tree_kill_tagged_callback function
f window_tree_menu function
f window_tree_mouse function
f window_tree_pull_item function
f window_tree_resize function
f window_tree_search function
f window_tree_sort function
f window_tree_swap function
f window_tree_update function
f window_unzoom function
f window_update_activity function
f window_update_focus function
f window_zoom function
f windows_RB_FIND function
f windows_RB_INSERT function
f windows_RB_INSERT_COLOR function
f windows_RB_MINMAX function
f windows_RB_NEXT function
f windows_RB_NFIND function
f windows_RB_PREV function
f windows_RB_REMOVE function
f windows_RB_REMOVE_COLOR function
f winlink_add function
f winlink_clear_flags function
f winlink_cmp function
f winlink_count function
f winlink_find_by_index function
f winlink_find_by_window function
f winlink_find_by_window_id function
f winlink_next function
f winlink_next_by_number function
f winlink_next_index function
f winlink_previous function
f winlink_previous_by_number function
f winlink_remove function
f winlink_set_window function
f winlink_shuffle_up function
f winlink_stack_push function
f winlink_stack_remove function
f winlinks_RB_FIND function
f winlinks_RB_INSERT function
f winlinks_RB_INSERT_COLOR function
f winlinks_RB_MINMAX function
f winlinks_RB_NEXT function
f winlinks_RB_NFIND function
f winlinks_RB_PREV function
f winlinks_RB_REMOVE function
f winlinks_RB_REMOVE_COLOR function
Pane 1 type, 7 functions and constants S window_pane struct 62 members
f window_pane_find_by_id function
f window_pane_at_index function
f window_pane_key function
f window_pane_paste function
f window_pane_resize function
f window_pane_set_mode function
f window_pane_reset_mode function
Pane — Supporting declarations 11 types, 70 functions and constants S window_mode struct 12 members
S window_mode_entry struct 8 members
S window_pane_input_data struct 3 members
S window_pane_offset struct 1 member
S window_pane_resize struct 6 members
S window_pane_resizes struct 2 members
S window_pane_tree struct 1 member
S window_panes struct 2 members
S window_panes_zindex struct 2 members
E anonymous enum enum 7 members
E anonymous enum enum 3 members
a client_exitreason attribute
k WINDOW_BUFFER_DEFAULT_COMMAND constant
k WINDOW_BUFFER_DEFAULT_FORMAT constant
k WINDOW_BUFFER_DEFAULT_KEY_FORMAT constant
k WINDOW_CLIENT_DEFAULT_COMMAND constant
k WINDOW_CLIENT_DEFAULT_FORMAT constant
k WINDOW_CLIENT_DEFAULT_KEY_FORMAT constant
k WINDOW_COPY_CMD_FLAG_READONLY constant
k WINDOW_COPY_DRAG_REPEAT_TIME constant
k WINDOW_COPY_SEARCH_ALL_TIMEOUT constant
k WINDOW_COPY_SEARCH_MAX_LINE constant
k WINDOW_COPY_SEARCH_TIMEOUT constant
k WINDOW_CUSTOMIZE_DEFAULT_FORMAT constant
k WINDOW_TREE_DEFAULT_COMMAND constant
k WINDOW_TREE_DEFAULT_FORMAT constant
k WINDOW_TREE_DEFAULT_KEY_FORMAT constant
f window_pane_border_status_get_range function
f window_pane_choose_best function
f window_pane_cmp function
f window_pane_copy_key function
f window_pane_copy_paste function
f window_pane_create function
f window_pane_default_cursor function
f window_pane_destroy function
f window_pane_destroy_ready function
f window_pane_error_callback function
f window_pane_exited function
f window_pane_find_by_id_str function
f window_pane_find_down function
f window_pane_find_left function
f window_pane_find_right function
f window_pane_find_up function
f window_pane_full_size_offset function
f window_pane_get_bg function
f window_pane_get_bg_control_client function
f window_pane_get_fg function
f window_pane_get_fg_control_client function
f window_pane_get_new_data function
f window_pane_get_palette function
f window_pane_get_theme function
f window_pane_index function
f window_pane_input_callback function
f window_pane_is_floating function
f window_pane_mode function
f window_pane_next_by_number function
f window_pane_previous_by_number function
f window_pane_printable_flags function
f window_pane_read_callback function
f window_pane_reset_mode_all function
f window_pane_search function
f window_pane_send_resize function
f window_pane_send_theme_update function
f window_pane_set_event function
f window_pane_show_scrollbar function
f window_pane_stack_push function
f window_pane_stack_remove function
f window_pane_start_input function
f window_pane_tree_RB_FIND function
f window_pane_tree_RB_INSERT function
f window_pane_tree_RB_INSERT_COLOR function
f window_pane_tree_RB_MINMAX function
f window_pane_tree_RB_NEXT function
f window_pane_tree_RB_NFIND function
f window_pane_tree_RB_PREV function
f window_pane_tree_RB_REMOVE function
f window_pane_tree_RB_REMOVE_COLOR function
f window_pane_update_focus function
f window_pane_update_used_data function
f window_pane_visible function
f window_pane_zindex function
Client 1 type, 6 functions and constants S client struct 90 members
f client_main function
f server_client_create function
f server_client_open function
f server_client_set_session function
f server_client_detach function
f server_client_lost function
Client — Supporting declarations 9 types, 128 functions and constants E anonymous enum enum 9 members
S client_file struct 15 members
S client_files struct 1 member
S client_window struct 6 members
S client_windows struct 1 member
S clients struct 2 members
S server_acl_entries struct 1 member
S server_acl_user struct 4 members
E client_theme enum 3 members
A client_file_cb type alias
a client_attached attribute
a client_execcmd attribute
a client_execshell attribute
a client_exitflag attribute
a client_exitmessage attribute
a client_exitsession attribute
a client_exittype attribute
a client_exitval attribute
a client_files attribute
a client_flags attribute
a client_peer attribute
a client_proc attribute
a client_suspended attribute
a clients attribute
a server_acl_entries attribute
k SERVER_ACL_READONLY constant
a server_client_flags attribute
f client_connect function
f client_dispatch function
f client_dispatch_attached function
f client_dispatch_exit_message function
f client_dispatch_wait function
f client_exec function
f client_exit function
f client_exit_message function
f client_file_check_cb function
f client_files_RB_FIND function
f client_files_RB_INSERT function
f client_files_RB_INSERT_COLOR function
f client_files_RB_MINMAX function
f client_files_RB_NEXT function
f client_files_RB_NFIND function
f client_files_RB_PREV function
f client_files_RB_REMOVE function
f client_files_RB_REMOVE_COLOR function
f client_get_lock function
f client_send_identify function
f client_signal function
f client_windows_RB_FIND function
f client_windows_RB_INSERT function
f client_windows_RB_INSERT_COLOR function
f client_windows_RB_MINMAX function
f client_windows_RB_NEXT function
f client_windows_RB_NFIND function
f client_windows_RB_PREV function
f client_windows_RB_REMOVE function
f client_windows_RB_REMOVE_COLOR function
f clients_calculate_size function
f clients_with_window function
f server_acl_cmp function
f server_acl_display function
f server_acl_entries_RB_FIND function
f server_acl_entries_RB_INSERT function
f server_acl_entries_RB_INSERT_COLOR function
f server_acl_entries_RB_MINMAX function
f server_acl_entries_RB_NEXT function
f server_acl_entries_RB_NFIND function
f server_acl_entries_RB_PREV function
f server_acl_entries_RB_REMOVE function
f server_acl_entries_RB_REMOVE_COLOR function
f server_acl_get_uid function
f server_acl_init function
f server_acl_join function
f server_acl_user_allow function
f server_acl_user_allow_write function
f server_acl_user_deny function
f server_acl_user_deny_write function
f server_acl_user_find function
f server_client_add_client_window function
f server_client_attached_lost function
f server_client_check_exit function
f server_client_check_modes function
f server_client_check_mouse function
f server_client_check_mouse_in_pane function
f server_client_check_nested function
f server_client_check_pane_buffer function
f server_client_check_pane_resize function
f server_client_check_redraw function
f server_client_check_window_resize function
f server_client_clear_overlay function
f server_client_click_timer function
f server_client_command_done function
f server_client_control_flags function
f server_client_default_command function
f server_client_dispatch function
f server_client_dispatch_command function
f server_client_dispatch_identify function
f server_client_dispatch_shell function
f server_client_ensure_ranges function
f server_client_exec function
f server_client_free function
f server_client_get_client_window function
f server_client_get_cwd function
f server_client_get_flags function
f server_client_get_key_table function
f server_client_get_pane function
f server_client_handle_key function
f server_client_how_many function
f server_client_is_assume_paste function
f server_client_is_bracket_paste function
f server_client_is_default_key_table function
f server_client_key_callback function
f server_client_key_table_activity_diff function
f server_client_loop function
f server_client_overlay_range function
f server_client_overlay_timer function
f server_client_print function
f server_client_ranges_is_empty function
f server_client_read_only function
f server_client_redraw_timer function
f server_client_remove_pane function
f server_client_repeat_time function
f server_client_repeat_timer function
f server_client_report_theme function
f server_client_reset_state function
f server_client_resize_timer function
f server_client_set_flags function
f server_client_set_key_table function
f server_client_set_overlay function
f server_client_set_pane function
f server_client_set_path function
f server_client_set_progress_bar function
f server_client_set_title function
f server_client_suspend function
f server_client_unref function
f server_client_update_latest function
f server_client_window_cmp function
Commands 5 types, 5 functions and constants S cmd struct 8 members
S cmd_entry struct 8 members
S args struct 3 members
S cmd_parse_result struct 3 members
S cmd_find_state struct 7 members
f cmd_parse_from_string function
f cmd_find_target function
f cmdq_get_command function
f cmdq_append function
f cmdq_next function
Commands — Supporting declarations 31 types, 422 functions and constants E cmdq_type enum 2 members
S args_command_state struct 3 members
S args_entry struct 6 members
S args_parse struct 4 members
S args_tree struct 1 member
S args_value struct 6 members
S args_values struct 2 members
S cmd_command_prompt_cdata struct 9 members
S cmd_command_prompt_prompt struct 2 members
S cmd_confirm_before_data struct 4 members
S cmd_display_panes_data struct 2 members
S cmd_entry_flag struct 3 members
S cmd_if_shell_data struct 4 members
S cmd_list struct 3 members
S cmd_load_buffer_data struct 3 members
S cmd_parse_input struct 6 members
S cmd_run_shell_data struct 9 members
S cmd_source_file_data struct 7 members
S cmdq_item struct 19 members
S cmdq_item_list struct 2 members
S cmdq_list struct 2 members
S cmdq_state struct 5 members
S cmds struct 2 members
S wait_channel struct 9 members
S wait_channels struct 1 member
S wait_item struct 3 members
E args_type enum 3 members
E args_parse_type enum 4 members
E cmd_find_type enum 3 members
E cmd_retval enum 4 members
E cmd_parse_status enum 2 members
A args_parse_cb type alias
k ARGS_ENTRY_OPTIONAL_VALUE constant
k BREAK_PANE_TEMPLATE constant
a cmd_attach_session_entry attribute
a cmd_bind_key_entry attribute
a cmd_break_pane_entry attribute
a cmd_capture_pane_entry attribute
a cmd_choose_buffer_entry attribute
a cmd_choose_client_entry attribute
a cmd_choose_tree_entry attribute
a cmd_clear_history_entry attribute
a cmd_clear_prompt_history_entry attribute
a cmd_clock_mode_entry attribute
a cmd_command_prompt_entry attribute
a cmd_confirm_before_entry attribute
a cmd_copy_mode_entry attribute
a cmd_customize_mode_entry attribute
a cmd_delete_buffer_entry attribute
a cmd_detach_client_entry attribute
a cmd_display_menu_entry attribute
a cmd_display_message_entry attribute
a cmd_display_panes_entry attribute
a cmd_display_popup_entry attribute
a cmd_find_pane_table attribute
a cmd_find_session_table attribute
a cmd_find_window_entry attribute
a cmd_find_window_table attribute
a cmd_has_session_entry attribute
a cmd_if_shell_entry attribute
a cmd_join_pane_entry attribute
a cmd_kill_pane_entry attribute
a cmd_kill_server_entry attribute
a cmd_kill_session_entry attribute
a cmd_kill_window_entry attribute
a cmd_last_pane_entry attribute
a cmd_last_window_entry attribute
a cmd_link_window_entry attribute
a cmd_list_buffers_entry attribute
a cmd_list_clients_entry attribute
a cmd_list_commands_entry attribute
a cmd_list_keys_entry attribute
a cmd_list_next_group attribute
a cmd_list_panes_entry attribute
a cmd_list_sessions_entry attribute
a cmd_list_windows_entry attribute
a cmd_load_buffer_entry attribute
a cmd_lock_client_entry attribute
a cmd_lock_server_entry attribute
a cmd_lock_session_entry attribute
a cmd_move_pane_entry attribute
a cmd_move_window_entry attribute
a cmd_new_pane_entry attribute
a cmd_new_session_entry attribute
a cmd_new_window_entry attribute
a cmd_next_layout_entry attribute
a cmd_next_window_entry attribute
a cmd_paste_buffer_entry attribute
a cmd_pipe_pane_entry attribute
a cmd_previous_layout_entry attribute
a cmd_previous_window_entry attribute
a cmd_refresh_client_entry attribute
a cmd_rename_session_entry attribute
a cmd_rename_window_entry attribute
a cmd_resize_pane_entry attribute
a cmd_resize_window_entry attribute
a cmd_respawn_pane_entry attribute
a cmd_respawn_window_entry attribute
a cmd_rotate_window_entry attribute
a cmd_run_shell_entry attribute
a cmd_save_buffer_entry attribute
a cmd_select_layout_entry attribute
a cmd_select_pane_entry attribute
a cmd_select_window_entry attribute
a cmd_send_keys_entry attribute
a cmd_send_prefix_entry attribute
a cmd_server_access_entry attribute
a cmd_set_buffer_entry attribute
a cmd_set_environment_entry attribute
a cmd_set_hook_entry attribute
a cmd_set_option_entry attribute
a cmd_set_window_option_entry attribute
a cmd_show_buffer_entry attribute
a cmd_show_environment_entry attribute
a cmd_show_hooks_entry attribute
a cmd_show_messages_entry attribute
a cmd_show_options_entry attribute
a cmd_show_prompt_history_entry attribute
a cmd_show_window_options_entry attribute
a cmd_source_file_depth attribute
k CMD_SOURCE_FILE_DEPTH_LIMIT constant
a cmd_source_file_entry attribute
a cmd_split_window_entry attribute
a cmd_start_server_entry attribute
a cmd_suspend_client_entry attribute
a cmd_swap_pane_entry attribute
a cmd_swap_window_entry attribute
a cmd_switch_client_entry attribute
a cmd_table attribute
a cmd_unbind_key_entry attribute
a cmd_unlink_window_entry attribute
a cmd_wait_for_entry attribute
k CMDQ_FIRED constant
k CMDQ_WAITING constant
k DISPLAY_MESSAGE_TEMPLATE constant
k LIST_BUFFERS_TEMPLATE constant
k LIST_CLIENTS_TEMPLATE constant
k LIST_COMMANDS_TEMPLATE constant
k LIST_KEYS_TEMPLATE constant
k LIST_SESSIONS_TEMPLATE constant
k LIST_WINDOWS_TEMPLATE constant
k LIST_WINDOWS_WITH_SESSION_TEMPLATE constant
k NEW_SESSION_TEMPLATE constant
k NEW_WINDOW_TEMPLATE constant
k SHOW_MESSAGES_TEMPLATE constant
k SPLIT_WINDOW_TEMPLATE constant
a wait_channels attribute
f args_cmp function
f args_copy function
f args_copy_copy_value function
f args_copy_value function
f args_count function
f args_create function
f args_escape function
f args_find function
f args_first function
f args_first_value function
f args_free function
f args_free_value function
f args_free_values function
f args_from_vector function
f args_get function
f args_has function
f args_make_commands function
f args_make_commands_free function
f args_make_commands_get_command function
f args_make_commands_now function
f args_make_commands_prepare function
f args_next function
f args_next_value function
f args_parse function
f args_parse_flag_argument function
f args_parse_flags function
f args_percentage function
f args_percentage_and_expand function
f args_print function
f args_print_add function
f args_print_add_value function
f args_set function
f args_string function
f args_string_percentage function
f args_string_percentage_and_expand function
f args_strtonum function
f args_strtonum_and_expand function
f args_to_vector function
f args_tree_RB_FIND function
f args_tree_RB_INSERT function
f args_tree_RB_INSERT_COLOR function
f args_tree_RB_MINMAX function
f args_tree_RB_NEXT function
f args_tree_RB_NFIND function
f args_tree_RB_PREV function
f args_tree_RB_REMOVE function
f args_tree_RB_REMOVE_COLOR function
f args_type_to_string function
f args_value function
f args_value_as_string function
f args_values function
f cmd_append_argv function
f cmd_attach_session function
f cmd_attach_session_exec function
f cmd_bind_key_args_parse function
f cmd_bind_key_exec function
f cmd_break_pane_exec function
f cmd_capture_pane_append function
f cmd_capture_pane_exec function
f cmd_capture_pane_history function
f cmd_capture_pane_hyperlinks function
f cmd_capture_pane_pending function
f cmd_choose_tree_args_parse function
f cmd_choose_tree_exec function
f cmd_command_prompt_args_parse function
f cmd_command_prompt_callback function
f cmd_command_prompt_exec function
f cmd_command_prompt_free function
f cmd_confirm_before_args_parse function
f cmd_confirm_before_callback function
f cmd_confirm_before_exec function
f cmd_confirm_before_free function
f cmd_copy function
f cmd_copy_argv function
f cmd_copy_mode_exec function
f cmd_detach_client_exec function
f cmd_display_menu_args_parse function
f cmd_display_menu_exec function
f cmd_display_menu_get_pos function
f cmd_display_message_each function
f cmd_display_message_exec function
f cmd_display_panes_args_parse function
f cmd_display_panes_draw function
f cmd_display_panes_draw_pane function
f cmd_display_panes_exec function
f cmd_display_panes_free function
f cmd_display_panes_key function
f cmd_display_panes_put function
f cmd_display_popup_exec function
f cmd_find function
f cmd_find_best_client function
f cmd_find_best_session function
f cmd_find_best_session_with_window function
f cmd_find_best_winlink_with_window function
f cmd_find_clear_state function
f cmd_find_client function
f cmd_find_client_better function
f cmd_find_copy_state function
f cmd_find_current_client function
f cmd_find_empty_state function
f cmd_find_from_client function
f cmd_find_from_mouse function
f cmd_find_from_nothing function
f

## 评论（1/1）

> **tony** · 2026-10-25T18:45:02.000Z　
> I made a tmux source reference, doxygen-inspired. It links C symbols to CLI commands, options, hooks, formats and libtmux APIs (including alpha ports to new languages like TypeScript, Rust, Go).Disclaimer: I used LLMs extensively to build this. I have intersection with building documentation systems and tmux. Also, I didn't create tmux itself, just a wrapper called libtmux and session manager for it.tmux is created by Nicholas Marriott, its official site is at https://github.com/tmux/tmux. I and others are very thankful to be able to use his program daily, and that it's still being well-maintained!P.S. there are PRs for introducing Sixel / Kitty-based terminal graphics in the pipe: https://github.com/tmux/tmux/pull/5445#issuecomment-61802179.... Very big stuff on the way. https://github.com/tmux/tmux/issues/5406

## 导航

- 项目页：[[10-项目/libtmux.org_19752476]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
