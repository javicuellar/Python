import 'package:flutter/material.dart';

import '../flet_control_backend.dart';
import '../models/control.dart';
import '../utils/edge_insets.dart';
import 'create_control.dart';
import 'flet_store_mixin.dart';

class ExpansionPanelListControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;

  const ExpansionPanelListControl(
      {super.key,
      this.parent,
      required this.control,
      required this.children,
      required this.parentDisabled,
      required this.parentAdaptive,
      required this.backend});

  @override
  State<ExpansionPanelListControl> createState() =>
      _ExpansionPanelListControlState();
}

class _ExpansionPanelListControlState extends State<ExpansionPanelListControl>
    with FletStoreMixin {
  @override
  Widget build(BuildContext context) {
    debugPrint("ExpansionPanelList build: ${widget.control.id}");
    bool disabled = widget.control.isDisabled || widget.parentDisabled;
    bool? adaptive =
        widget.control.attrBool("adaptive") ?? widget.parentAdaptive;

    var panels = widget.children
        .where((c) => c.name == "expansionpanel" && c.isVisible)
        .toList();

    void onChange(int index, bool isExpanded) {
      widget.backend.updateControlState(
          panels[index].id, {"expanded": isExpanded.toString().toLowerCase()});
      widget.backend.triggerControlEvent(widget.control.id, "change", "$index");
    }

    var panelList =
        withControls(panels.map((p) => p.id), (content, panelViews) {
      return ExpansionPanelList(
          elevation: widget.control.attrDouble("elevation", 2)!,
          materialGapSize: widget.control.attrDouble("spacing", 16)!,
          dividerColor: widget.control.attrColor("dividerColor", context),
          expandIconColor:
              widget.control.attrColor("expandedIconColor", context),
          expandedHeaderPadding: parseEdgeInsets(
              widget.control,
              "expandedHeaderPadding",
              const EdgeInsets.symmetric(vertical: 16))!,
          expansionCallback: !disabled
              ? (int index, bool isExpanded) {
                  onChange(index, isExpanded);
                }
              : null,
          children: panelViews.controlViews.map((panelView) {
            var headerCtrls = panelView.children
                .where((c) => c.name == "header" && c.isVisible);
            var bodyCtrls = panelView.children
                .where((c) => c.name == "content" && c.isVisible);

            return ExpansionPanel(
              backgroundColor: panelView.control.attrColor("bgColor", context),
              isExpanded: panelView.control.attrBool("expanded", false)!,
              highlightColor:
                  panelView.control.attrColor("highlightColor", context),
              splashColor: panelView.control.attrColor("splashColor", context),
              canTapOnHeader:
                  panelView.control.attrBool("canTapHeader", false)!,
              headerBuilder: (BuildContext context, bool isExpanded) {
                return headerCtrls.isNotEmpty
                    ? createControl(
                        widget.control, headerCtrls.first.id, disabled,
                        parentAdaptive: adaptive)
                    : const ListTile(title: Text("Header Placeholder"));
              },
              body: bodyCtrls.isNotEmpty
                  ? createControl(widget.control, bodyCtrls.first.id, disabled,
                      parentAdaptive: adaptive)
                  : const ListTile(title: Text("Body Placeholder")),
            );
          }).toList());
    });

    return constrainedControl(
        context, panelList, widget.parent, widget.control);
  }
}
