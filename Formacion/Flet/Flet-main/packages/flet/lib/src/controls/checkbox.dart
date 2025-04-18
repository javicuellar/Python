import 'package:collection/collection.dart';
import 'package:flutter/material.dart';

import '../flet_control_backend.dart';
import '../models/control.dart';
import '../utils/borders.dart';
import '../utils/colors.dart';
import '../utils/mouse.dart';
import '../utils/others.dart';
import '../utils/text.dart';
import '../utils/theme.dart';
import 'create_control.dart';
import 'cupertino_checkbox.dart';
import 'flet_store_mixin.dart';
import 'list_tile.dart';

class CheckboxControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;
  final List<Control> children;

  const CheckboxControl(
      {super.key,
      this.parent,
      required this.control,
      required this.parentDisabled,
      required this.parentAdaptive,
      required this.children,
      required this.backend});

  @override
  State<CheckboxControl> createState() => _CheckboxControlState();
}

class _CheckboxControlState extends State<CheckboxControl> with FletStoreMixin {
  bool? _value;
  bool _tristate = false;
  late final FocusNode _focusNode;

  @override
  void initState() {
    super.initState();
    _focusNode = FocusNode();
    _focusNode.addListener(_onFocusChange);
  }

  void _onFocusChange() {
    widget.backend.triggerControlEvent(
        widget.control.id, _focusNode.hasFocus ? "focus" : "blur");
  }

  @override
  void dispose() {
    _focusNode.removeListener(_onFocusChange);
    _focusNode.dispose();
    super.dispose();
  }

  void _toggleValue() {
    bool? newValue;
    if (!_tristate) {
      newValue = !_value!;
    } else if (_tristate && _value == null) {
      newValue = false;
    } else if (_tristate && _value == false) {
      newValue = true;
    }
    _onChange(newValue);
  }

  void _onChange(bool? value) {
    var svalue = value != null ? value.toString() : "";
    _value = value;
    widget.backend.updateControlState(widget.control.id, {"value": svalue});
    widget.backend.triggerControlEvent(widget.control.id, "change", svalue);
  }

  @override
  Widget build(BuildContext context) {
    debugPrint("Checkbox build: ${widget.control.id}");

    return withPagePlatform((context, platform) {
      bool? adaptive =
          widget.control.attrBool("adaptive") ?? widget.parentAdaptive;
      bool disabled = widget.control.isDisabled || widget.parentDisabled;
      double? width = widget.control.attrDouble("width");
      double? height = widget.control.attrDouble("height");

      if (adaptive == true &&
          (platform == TargetPlatform.iOS ||
              platform == TargetPlatform.macOS)) {
        return CupertinoCheckboxControl(
            control: widget.control,
            parentDisabled: widget.parentDisabled,
            backend: widget.backend);
      }
      var label = widget.children.firstWhereOrNull((c) => c.isVisible);
      String labelStr = widget.control.attrString("label", "")!;
      LabelPosition labelPosition = parseLabelPosition(
          widget.control.attrString("labelPosition"), LabelPosition.right)!;
      _tristate = widget.control.attrBool("tristate", false)!;
      bool autofocus = widget.control.attrBool("autofocus", false)!;
      bool? value = widget.control.attrBool("value", _tristate ? null : false);
      if (_value != value) {
        _value = value;
      }

      TextStyle? labelStyle =
          parseTextStyle(Theme.of(context), widget.control, "labelStyle");
      if (disabled && labelStyle != null) {
        labelStyle = labelStyle.apply(color: Theme.of(context).disabledColor);
      }

      var checkbox = Checkbox(
          autofocus: autofocus,
          focusNode: _focusNode,
          value: _value,
          isError: widget.control.attrBool("isError", false)!,
          semanticLabel: widget.control.attrString("semanticsLabel"),
          shape: parseOutlinedBorder(widget.control, "shape"),
          side: parseWidgetStateBorderSide(
              Theme.of(context), widget.control, "borderSide"),
          splashRadius: widget.control.attrDouble("splashRadius"),
          activeColor: widget.control.attrColor("activeColor", context),
          focusColor: widget.control.attrColor("focusColor", context),
          hoverColor: widget.control.attrColor("hoverColor", context),
          overlayColor: parseWidgetStateColor(
              Theme.of(context), widget.control, "overlayColor"),
          checkColor: widget.control.attrColor("checkColor", context),
          fillColor: parseWidgetStateColor(
              Theme.of(context), widget.control, "fillColor"),
          tristate: _tristate,
          visualDensity:
              parseVisualDensity(widget.control.attrString("visualDensity")),
          mouseCursor:
              parseMouseCursor(widget.control.attrString("mouseCursor")),
          onChanged: !disabled
              ? (bool? value) {
                  _onChange(value);
                }
              : null);

      ListTileClicks.of(context)?.notifier.addListener(() {
        _toggleValue();
      });

      Widget result = checkbox;
      if (label != null || (labelStr != "")) {
        Widget? labelWidget;
        if (label != null) {
          labelWidget =
              createControl(widget.control, label.id, disabled);
        } else {
          labelWidget = disabled
              ? Text(labelStr, style: labelStyle)
              : MouseRegion(
                  cursor: SystemMouseCursors.click,
                  child: Text(labelStr, style: labelStyle));
        }

        result = MergeSemantics(
            child: GestureDetector(
                onTap: !disabled ? _toggleValue : null,
                child: labelPosition == LabelPosition.right
                    ? Row(children: [checkbox, labelWidget])
                    : Row(children: [labelWidget, checkbox])));
      }
      if (width != null || height != null) {
        result = SizedBox(
          width: width,
          height: height,
          child: FittedBox(
            fit: BoxFit.fill,
            child: result,
          ),
        );
      }

      return constrainedControl(context, result, widget.parent, widget.control);
    });
  }
}
